#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import numpy as np


def calc_prob_forward(A, B, pi, O):
    N, _x = A.shape
    assert (_x == N)
    _x, M = B.shape
    assert (_x == N)
    T = len(O)
    assert (len(pi) == N)

    # 观察到第一个序列，并且分布在每个状态的概率
    alpha = B[:, O[0]].T * pi
    alphas = list()
    # print(ob_dist)
    alphas.append(alpha)
    for i in range(1, T):
        # 状态概率的转移
        status_dist = np.dot(alpha, A)
        # 观察到第i个序列，并且分布在每个状态的概率
        next_alpha = B[:, O[i]].T * status_dist
        # print(next_alpha)
        alpha = next_alpha
        alphas.append(alpha)
    return np.sum(alpha), np.array(alphas)


def calc_prob_backward(A, B, pi, O):
    N, _x = A.shape
    assert (_x == N)
    _x, M = B.shape
    assert (_x == N)
    T = len(O)
    assert (len(pi) == N)

    # 假设最后可以停留在任何状态上
    # 然后从每一种状态倒推
    beta = np.ones(N)
    betas = list()
    # print(beta)
    for i in range(T - 1, 0, -1):
        status_dist = B[:, O[i]].T * beta
        next_beta = np.dot(status_dist, A.T)
        # print(next_beta)
        beta = next_beta
        betas.append(beta)
    beta = B[:, O[0]].T * beta * pi
    betas.append(beta)
    return np.sum(beta), np.array(betas)


# 计算某个时刻的概率分布
def calc_prob_t(alphas, betas, t, i):
    alpha = alphas[t][i]
    beta = betas[t][i]
    return alpha * beta / np.sum(alphas[t] * betas[t])


def calc_prob_t_batch(alphas, betas):
    a0 = alphas * betas
    a1 = np.sum(a0, axis=1)
    return a0 / a1.reshape((-1, 1))


# 计算t到t+1时刻从状态i转移到j的概率
def calc_prob_t2(alphas, betas, A, B, O, t, i, j):
    N, _ = A.shape
    a0 = alphas[t]
    a1 = A
    a2 = B[:, O[t + 1]]
    a3 = betas[t + 1]

    # note(yan): 这个地方需要对照图才能写正确
    den = 0.0
    for _x in range(N):
        for _y in range(N):
            den += a0[_x] * a1[_x, _y] * a2[_y] * a3[_y]
    a4 = a1 * a2 * a3
    num = (a0.reshape((-1, 1)) * a4)
    den2 = np.sum(num)
    den3 = np.sum(a0 * np.sum(a4, axis=1))
    assert (np.allclose(den, den2))
    assert (np.allclose(den2, den3))

    num = a0[i] * a1[i, j] * a2[j] * a3[j]
    return num / den


def calc_prob_t2_batch(alphas, betas, A, B, O, t):
    a0 = alphas[t]
    a1 = A
    a2 = B[:, O[t + 1]]
    a3 = betas[t + 1]
    a4 = a1 * a2 * a3
    num = a0.reshape((-1, 1)) * a4
    den = np.sum(num)
    return num / den


def test():
    A = np.array([[0.5, 0.2, 0.3],
                  [0.3, 0.5, 0.2],
                  [0.2, 0.3, 0.5]])
    B = np.array([[0.5, 0.5],
                  [0.4, 0.6],
                  [0.7, 0.3]])

    N, _ = A.shape

    # print(A)
    # print(B)
    pi = (0.2, 0.4, 0.4)
    O = (0, 1, 0)
    T = len(O)
    exp_prob = 0.130218

    # 前后向算法计算出来的alpha和beta
    prob, alphas = calc_prob_forward(A, B, pi, O)
    print('========== alphas ==========')
    print(prob)
    print(alphas)
    assert (np.allclose(prob, exp_prob))

    prob, betas = calc_prob_backward(A, B, pi, O)
    print('========== betas ==========')
    print(prob)
    print(betas)
    assert (np.allclose(prob, exp_prob))

    print('========== gamma ==========')

    probs = []
    for t in range(T):
        sub_probs = []
        for i in range(N):
            prob_t = calc_prob_t(alphas, betas, t, i)
            sub_probs.append(prob_t)
        assert (np.allclose(sum(sub_probs), 1.0))
        probs.append(sub_probs)
    probs0 = np.array(probs)
    print(probs0)

    probs1 = calc_prob_t_batch(alphas, betas)
    print(probs1)

    assert (np.allclose(probs0, probs1))

    print('========== ksi ==========')

    trans = []
    for i in range(N):
        sub_trans = []
        for j in range(N):
            prob_t2 = calc_prob_t2(alphas, betas, A, B, O, 1, i, j)
            sub_trans.append(prob_t2)
        trans.append(sub_trans)
    probs0 = np.array(trans)
    assert (np.allclose(np.sum(probs0), 1.0))
    print(probs0)

    probs1 = calc_prob_t2_batch(alphas, betas, A, B, O, 1)
    print(probs1)


def norm(x):
    xn = np.sum(x, axis=1)
    return x / xn.reshape((-1, 1))


def norm1d(x):
    return x / np.sum(x)


class HMM(object):
    def __init__(self, N, M):
        self.A = np.zeros((N, N))
        self.B = np.zeros((N, M))
        self.pi = np.ones(N) / N
        self.N = N
        self.M = M

        x = np.random.rand(N, N)
        self.A = norm(x)
        x = np.random.rand(N, M)
        self.B = norm(x)
        # x = np.random.rand(N)
        # self.pi = norm1d(x)

    def train_once(self, O):
        _, alphas = calc_prob_forward(self.A, self.B, self.pi, O)
        _, betas = calc_prob_backward(self.A, self.B, self.pi, O)
        T = len(O)
        N = self.N
        M = self.M

        # a{ij}
        ksi = np.zeros((N, N)) + 0.001
        for t in range(T - 1):
            t2 = calc_prob_t2_batch(alphas, betas, self.A, self.B, O, t)
            ksi += t2
        # print(ksi)
        # print(self.A)
        # print(self.B)
        gamma = calc_prob_t_batch(alphas, betas)
        trans = np.sum(gamma[:-1], axis=0)
        A = ksi / trans
        A = norm(A)
        # print(A)
        assert (np.allclose(np.sum(A, axis=1), np.ones(N)))

        # b{jk}
        B = np.zeros((M, N))
        for k in range(M):
            prob = np.zeros(N) + 0.001
            for t in range(T):
                if O[t] == k:
                    prob += gamma[t]
            B[k] = prob / (np.sum(gamma, axis=0))
        B = B.T
        B = norm(B)
        assert (np.allclose(np.sum(B, axis=1), np.ones(N)))

        pi = gamma[0]
        return A, B, pi

    def train(self, O, n_seq=10, n_step=3, n_iter=100):
        T = len(O)
        count = 0
        for i in range(n_iter):
            idx = 0
            while (idx + n_seq) < T:
                subO = O[idx: idx + n_seq]
                # print('trained O = {}'.format(subO))
                idx += n_step
                A, B, pi = self.train_once(subO)
                count += 1
                # if np.abs(np.min(A)) < 1e-50 or np.abs(np.min(B)) < 1e-50:
                #     print('trained # of seqs = %d' % count)
                #     return
                self.A = A
                self.B = B
                self.pi = pi

    def choose(self, prob):
        assert (len(prob.shape) == 1)
        xs = np.arange(len(prob))
        return np.random.choice(xs, p=prob)

    def generate(self, n):
        ss = []
        output = []
        s0 = self.choose(self.pi)
        ss.append(s0)
        output.append(self.choose(self.B[s0]))
        for i in range(n):
            s1 = self.choose(self.A[s0])
            ss.append(s1)
            output.append(self.choose(self.B[s1]))
            s0 = s1
        return ss, output


if __name__ == '__main__':
    test()
    print('========== hmm ===========')
    hmm = HMM(N=100, M=6)
    O = [0, 1, 3, 5, 4] * 3
    hmm.train(O, n_iter=100)
    ss, output = hmm.generate(20)
    print(output)
    # print(hmm.A)
