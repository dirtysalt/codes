下面是运行结果，其中FAST是使用 `stride=8` 跑出来的

```
YAN007 :: ~/shared/MatrixTranspose ‹master*› » ./a.out
[SLOW, S=8] N = 1010, took: 1533ms, avg 1502.79ns/N
[FAST, S=8] N = 1010, took: 1582ms, avg 1550.83ns/N
[SLOW, S=8] N = 1024, took: 10529ms, avg 10041.2ns/N
[FAST, S=8] N = 1024, took: 2382ms, avg 2271.65ns/N
[SLOW, S=8] N = 1030, took: 1628ms, avg 1534.55ns/N
[FAST, S=8] N = 1030, took: 1467ms, avg 1382.79ns/N
```

此时stride设置是8，可以看到效果还是不错的，对于N=1030有所改进，对于N=1024来说提升就特别大。

如果cache size = 64KB, ways = 4, line size = 64, 矩阵是1024 * 1024的话，那么：
1. 相邻两个row, 地址差距是 1024 * 4 = 4kB
2. cache size = 64KB, line size = 64, 那么一共有1KB个lines
3. 所以理论上两个row都会落在一个line上，但是因为ways=4, 所以可以忍受4个冲突。

不过如果是使用SLOW的方法，cache是没有办法忍受冲突的，因此是按照行扫描下来的，然后继续从0行开始扫描，而此时缓存已经全部被换出了。

在Linux下面可以查看cache的配置

```
YAN007 :: ~/shared/MatrixTranspose ‹master*› » getconf -a | grep CACHE
LEVEL1_ICACHE_SIZE                 32768
LEVEL1_ICACHE_ASSOC                8
LEVEL1_ICACHE_LINESIZE             64
LEVEL1_DCACHE_SIZE                 32768
LEVEL1_DCACHE_ASSOC                8
LEVEL1_DCACHE_LINESIZE             64
LEVEL2_CACHE_SIZE                  1048576
LEVEL2_CACHE_ASSOC                 16
LEVEL2_CACHE_LINESIZE              64
LEVEL3_CACHE_SIZE                  20185088
LEVEL3_CACHE_ASSOC                 11
LEVEL3_CACHE_LINESIZE              64
LEVEL4_CACHE_SIZE                  0
LEVEL4_CACHE_ASSOC                 0
LEVEL4_CACHE_LINESIZE              0
```

这里看L1D和L2配置，好像L3的效果就不明显了。
- L1D：32KB，8ways，64B
- L2: 1024KB, 16ways, 64B

处理1024*1024的矩阵，从L1D上看最多承受8个冲突，从L2上看最多承受64个冲突。然后因为line size = 64B, 最多可以放入16个int.
如果我们想提高L1D的cache命中率，stride就不能超过8个，考虑到按照行本身需要占用1个cache line, 所以stride估计设置成为7个是最好的。

下面是 `stride=7` 的效果
```
YAN007 :: ~/shared/MatrixTranspose ‹master*› » ./a.out
[SLOW, S=7] N = 1010, took: 1513ms, avg 1483.19ns/N
[FAST, S=7] N = 1010, took: 1637ms, avg 1604.74ns/N
[SLOW, S=7] N = 1024, took: 10520ms, avg 10032.7ns/N
[FAST, S=7] N = 1024, took: 2339ms, avg 2230.64ns/N
[SLOW, S=7] N = 1030, took: 1627ms, avg 1533.6ns/N
[FAST, S=7] N = 1030, took: 1490ms, avg 1404.47ns/N
```

下面是 `stride=6` 的效果
```
YAN007 :: ~/shared/MatrixTranspose ‹master*› » ./a.out
[SLOW, S=6] N = 1010, took: 1528ms, avg 1497.89ns/N
[FAST, S=6] N = 1010, took: 1620ms, avg 1588.08ns/N
[SLOW, S=6] N = 1024, took: 10528ms, avg 10040.3ns/N
[FAST, S=6] N = 1024, took: 2398ms, avg 2286.91ns/N
[SLOW, S=6] N = 1030, took: 1635ms, avg 1541.14ns/N
[FAST, S=6] N = 1030, took: 1507ms, avg 1420.49ns/N
```

下面是 `stride=9` 的效果，这个估计会稍微查一些，因为在处理一个stride的时候回产生`stride`次cache miss

```
YAN007 :: ~/shared/MatrixTranspose ‹master*› » ./a.out
[SLOW, S=9] N = 1010, took: 1514ms, avg 1484.17ns/N
[FAST, S=9] N = 1010, took: 1531ms, avg 1500.83ns/N
[SLOW, S=9] N = 1024, took: 10612ms, avg 10120.4ns/N
[FAST, S=9] N = 1024, took: 3489ms, avg 3327.37ns/N
[SLOW, S=9] N = 1030, took: 1653ms, avg 1558.11ns/N
[FAST, S=9] N = 1030, took: 1450ms, avg 1366.76ns/N
```
