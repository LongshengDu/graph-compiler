if(GC_ENABLE_DNNL_API)
    list(APPEND TABLEGEN_MACROS -DGC_HAS_ONEDNN_DIALECT)
endif()
if(GC_ENABLE_IMEX)
    list(APPEND TABLEGEN_MACROS -DGC_USE_IMEX)
endif()

set(LLVM_TARGET_DEFINITIONS Passes.td)
mlir_tablegen(Passes.h.inc -gen-pass-decls -name GraphCompiler ${TABLEGEN_MACROS})
mlir_tablegen(Passes.capi.h.inc -gen-pass-capi-header --prefix GraphCompiler)
mlir_tablegen(Passes.capi.cpp.inc -gen-pass-capi-impl --prefix GraphCompiler)
add_public_tablegen_target(GraphCompilerPassIncGen)
add_mlir_doc(Passes GraphCompilerPasses ./ -gen-pass-doc)

add_subdirectory(Microkernel)
