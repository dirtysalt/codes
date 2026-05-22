#include <quickjs/quickjs-libc.h>
#include <quickjs/quickjs.h>

static const char* FILENAME = "test.js";

static JSContext* JS_NewCustomContext(JSRuntime* rt) {
    JSContext* ctx = JS_NewContextRaw(rt);
    if (!ctx) return NULL;
    JS_AddIntrinsicBaseObjects(ctx);
    JS_AddIntrinsicDate(ctx);
    JS_AddIntrinsicEval(ctx);
    JS_AddIntrinsicStringNormalize(ctx);
    JS_AddIntrinsicRegExp(ctx);
    JS_AddIntrinsicJSON(ctx);
    JS_AddIntrinsicProxy(ctx);
    JS_AddIntrinsicMapSet(ctx);
    JS_AddIntrinsicTypedArrays(ctx);
    JS_AddIntrinsicPromise(ctx);
    JS_AddIntrinsicBigInt(ctx);
    return ctx;
}

static JSValue js_add(JSContext* ctx, JSValueConst this_val, int argc, JSValueConst* argv) {
    int32_t a = JS_VALUE_GET_INT(argv[0]);
    int32_t b = JS_VALUE_GET_INT(argv[1]);
    return JS_NewInt32(ctx, a + b);
}

static void add_native_functions(JSContext* ctx) {
    JSValue global_obj = JS_GetGlobalObject(ctx);
    JS_SetPropertyStr(ctx, global_obj, "add", JS_NewCFunction(ctx, js_add, "add", 2));
    JS_FreeValue(ctx, global_obj);
}

void eval_file(JSContext* ctx, const char* filename) {
    size_t buf_len = 0;
    uint8_t* data = js_load_file(ctx, &buf_len, filename);
    JSValue ret = JS_Eval(ctx, (const char*)data, buf_len, FILENAME, JS_EVAL_TYPE_GLOBAL);
    if (JS_IsException(ret)) {
        JSValue exception_val = JS_GetException(ctx);

        const char* exception_str = JS_ToCString(ctx, exception_val);
        if (exception_str) {
            printf("%s\n", exception_str);
            JS_FreeCString(ctx, exception_str);
        }

        JSValue stack = JS_GetPropertyStr(ctx, exception_val, "stack");
        if (!JS_IsUndefined(stack)) {
            const char* stack_str = JS_ToCString(ctx, stack);
            printf("Stack trace:\n%s\n", stack_str);
            JS_FreeCString(ctx, stack_str);
        }
        JS_FreeValue(ctx, stack);
        JS_FreeValue(ctx, exception_val);
    }
    JS_FreeValue(ctx, ret);
}

int main(int argc, char** argv) {
    JSRuntime* rt;
    JSContext* ctx;
    rt = JS_NewRuntime();
    js_std_set_worker_new_context_func(JS_NewCustomContext);
    js_std_init_handlers(rt);
    JS_SetModuleLoaderFunc(rt, NULL, js_module_loader, NULL);
    ctx = JS_NewCustomContext(rt);
    js_std_add_helpers(ctx, argc, argv);

    add_native_functions(ctx);
    eval_file(ctx, FILENAME);

    // js_std_eval_binary(ctx, qjsc_test, qjsc_test_size, 0);

    js_std_loop(ctx);
    js_std_free_handlers(rt);
    JS_FreeContext(ctx);
    JS_FreeRuntime(rt);
    return 0;
}
