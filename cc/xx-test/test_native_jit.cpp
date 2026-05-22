#include <iostream>
#include <sstream>

#include "NativeJIT/CodeGen/ExecutionBuffer.h"
#include "NativeJIT/CodeGen/FunctionBuffer.h"
#include "NativeJIT/Function.h"
#include "Temporary/Allocator.h"

using NativeJIT::Allocator;
using NativeJIT::ExecutionBuffer;
using NativeJIT::Function;
using NativeJIT::FunctionBuffer;

int main() {
    ExecutionBuffer codeAllocator(8192);
    Allocator allocator(8192);
    FunctionBuffer code(codeAllocator, 8192);

    const float PI = 3.14159265358979f;

    Function<float, float> expression(allocator, code);
    std::ostringstream oss;
    code.EnableDiagnostics(oss);

    auto& a = expression.Mul(expression.GetP1(), expression.GetP1());
    auto& b = expression.Mul(a, expression.Immediate(PI));
    auto function = expression.Compile(b);

    float p1 = 2.0;

    auto expected = PI * p1 * p1;
    auto observed = function(p1);

    std::cout << expected << " == " << observed << std::endl;
    std::cout << oss.str() << std::endl;
    return 0;
}