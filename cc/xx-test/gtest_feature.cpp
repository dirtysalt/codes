
#include <gtest/gtest-param-test.h>
#include <gtest/gtest.h>

#include <cstdio>
#include <vector>

// In order to run tests more faster, we are using the gtest-parallel script(https://github.com/google/gtest-parallel)
// to execute test binaries. Since many of our test cases use globally-shared resources and cannot be run in parallel,
// gtest-parallel must be executed with the option `--serialize_test_cases`, which will run tests within the same test
// case sequentially.
// The PARALLEL_TEST is just a simple wrapper on TEST to give each test a unique case name, make them be able to run
// in parallel.
#define TOKENPASTE(x, y) x##y
#define TOKENPASTE2(x, y) TOKENPASTE(x, y)
#define PARALLEL_TEST(test_case_name, test_name) TEST(TOKENPASTE2(test_case_name, __LINE__), test_name)

using namespace std;
class VectorSize {
public:
    template <typename T>
    static int getVectorSize(const vector<T>& x) {
        return x.size();
    }
};

class VectorSizeTestFixture : public ::testing::Test {
public:
    void SetUp() override { fprintf(stderr, "SetUp...\n"); }
    void TearDown() override { fprintf(stderr, "TearDown...\n"); }
};

class VectorSizeTestParam : public ::testing::TestWithParam<std::tuple<std::vector<std::string>, int>> {};

PARALLEL_TEST(VectorSizeTest, test_int) {
    struct Case {
        std::vector<int> input;
        int output;
    };

    std::vector<Case> data = {Case{{1, 2, 3, 4}, 4}, Case{{1, 2, 3, 4, 5}, 5}};
    for (const auto& c : data) {
        EXPECT_EQ(VectorSize::getVectorSize(c.input), c.output);
    }
}

TEST_F(VectorSizeTestFixture, test_int) {
    struct Case {
        std::vector<int> input;
        int output;
    };

    std::vector<Case> data = {Case{{1, 2, 3, 4}, 4}, Case{{1, 2, 3, 4, 5}, 5}};
    for (const auto& c : data) {
        EXPECT_EQ(VectorSize::getVectorSize(c.input), c.output);
    }
}

TEST_F(VectorSizeTestFixture, test_double) {
    struct Case {
        std::vector<double> input;
        int output;
    };

    std::vector<Case> data = {Case{{10.1, 20.2}, 2}, Case{{10.3, 20.4, 20.3}, 3}};
    for (const auto& c : data) {
        EXPECT_EQ(VectorSize::getVectorSize(c.input), c.output);
    }
}

TEST_P(VectorSizeTestParam, test_string) {
    const std::vector<std::string>& input = std::get<0>(GetParam());
    int output = std::get<1>(GetParam());
    EXPECT_EQ(VectorSize::getVectorSize(input), output);
}

INSTANTIATE_TEST_SUITE_P(VectorSizeTestSpace, VectorSizeTestParam,
                         ::testing::Values(std::make_tuple(std::vector<std::string>{}, 0),
                                           std::make_tuple(std::vector<std::string>{"hello", "world"}, 2)));
