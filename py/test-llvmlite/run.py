"""
This file demonstrates a trivial function "fpadd" returning the sum of
two floating-point numbers.
"""

from ctypes import CFUNCTYPE, POINTER, c_double, c_int8

import llvmlite.binding as llvm
from llvmlite import ir

# All these initializations are required for code generation!
llvm.initialize()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()  # yes, even this one
llvm.load_library_permanently('./libio.so')

# Create some useful types
# (double*, int8) -> double
double = ir.DoubleType()
double_ptr = double.as_pointer()
int8 = ir.IntType(8)
int32 = ir.IntType(32)
fnty = ir.FunctionType(double, (double_ptr, ir.IntType(8)))

# Create an empty module...
module = ir.Module(name=__file__)
# and declare a function named "fpadd" inside it
func = ir.Function(module, fnty, name="foo")

# Now implement the function
# return vec[idx] + 23.3
block = func.append_basic_block(name="entry")
builder = ir.IRBuilder(block)
vec, idx = func.args
ptr = builder.gep(vec, [idx], name="ptr")
tmp = builder.load(ptr, name="tmp")
result = builder.fadd(tmp, ir.Constant(double, 23.3), name="res")

write_fnty = ir.FunctionType(ir.VoidType(), (ir.IntType(8), ir.IntType(32)))
write_func=ir.Function(module,write_fnty,name="sys_write")
builder.call(write_func, (int8(ord('A')), int32(10)))
builder.call(write_func, (int8(ord('\n')), int32(2)))

true_blocker = func.append_basic_block(name = 'true_b')
false_blocker = func.append_basic_block(name = 'false_b')
end_block = func.append_basic_block(name = 'end_b')

cond = builder.icmp_signed('<=', int8(10), int8(9))
builder.cbranch(cond, true_blocker, false_blocker)

true_builder = ir.IRBuilder(true_blocker)
true_builder.call(write_func, (int8(ord('C')), int32(10)))
true_builder.branch(end_block)

false_builder = ir.IRBuilder(false_blocker)
false_builder.call(write_func, (int8(ord('D')), int32(10)))
false_builder.branch(end_block)

builder.position_at_end(end_block)
builder.call(write_func, (int8(ord('\n')), int32(2)))
builder.ret(result)

# Print the module IR
print(module)


# ====================

def create_execution_engine():
    """
    Create an ExecutionEngine suitable for JIT code generation on
    the host CPU.  The engine is reusable for an arbitrary number of
    modules.
    """
    # Create a target machine representing the host
    target = llvm.Target.from_default_triple()
    target_machine = target.create_target_machine()
    # And an execution engine with an empty backing module
    backing_mod = llvm.parse_assembly("")
    engine = llvm.create_mcjit_compiler(backing_mod, target_machine)
    return target_machine, engine


def compile_ir(engine, llvm_ir):
    """
    Compile the LLVM IR string with the given engine.
    The compiled module object is returned.
    """
    # Create a LLVM module object from the IR
    mod = llvm.parse_assembly(llvm_ir)
    mod.verify()
    # Now add the module and make sure it is ready for execution
    engine.add_module(mod)
    engine.finalize_object()
    engine.run_static_constructors()
    return mod


target_machine, engine = create_execution_engine()
mod = compile_ir(engine, str(module))
print(target_machine.emit_assembly(mod))

# Look up the function pointer (a Python int)
func_ptr = engine.get_function_address("foo")
cfunc = CFUNCTYPE(c_double, POINTER(c_double), c_int8)(func_ptr)
import numpy as np

arr = np.random.randint(100, 200, size=100).astype(np.float64)
ptr = arr.ctypes.data_as(POINTER(c_double))
res = cfunc(ptr, 56)
print(res)
