gc_set_mlir_link_components(MLIR_LINK_COMPONENTS MLIRIR)

include(onednn)

gc_add_mlir_library(MLIRMicrokernelTransforms
	ConvertLinalgToMicrokernel.cpp
        ExpandMicrokernel.cpp
        ConvertMicrokernelToDnnlFunc.cpp
        EarlyDispatchMicrokernel.cpp
        MicrokernelInvariantCodeMotion.cpp
        MergeBranchMicrokernelContext.cpp

        ADDITIONAL_HEADER_DIRS
        ${PROJECT_SOURCE_DIR}/include/

        DEPENDS
	MLIRMicrokernelPassesIncGen

        LINK_LIBS PUBLIC
        ${MLIR_LINK_COMPONENTS}
        GcInterface 
	GcUtilsIR
        MLIRMicrokernel
        )

get_property(GC_DNNL_INCLUDES GLOBAL PROPERTY GC_DNNL_INCLUDES)

target_include_directories(MLIRMicrokernelTransforms PUBLIC ${GC_DNNL_INCLUDES})
