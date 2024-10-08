################################################################################
# Copyright 2024 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
################################################################################

from typing import Dict, Tuple

import benchgc.util
import torch
from benchgc.mlir.util import MLIRCache
from gc_mlir import ir


def ref_constant(
    cache: MLIRCache, op: ir.OpView, var: Dict[str, torch.Tensor]
) -> Tuple[torch.Tensor, ...]:
    value = op.attributes["value"]
    if isinstance(value, ir.FloatAttr):
        return (
            torch.full(size=tuple(), fill_value=value.__float__(), dtype=torch.float),
        )
    elif isinstance(value, ir.DenseFPElementsAttr):
        if value.is_splat:
            return (
                torch.full(
                    size=tuple(value.type.shape),
                    fill_value=value.get_splat_value().value,
                    dtype=benchgc.util.get_dtype(str(value.get_splat_value().type)),
                ),
            )
        else:
            raise Exception("only support splat value now")
    elif isinstance(value, ir.IntegerAttr):
        return (torch.full(size=tuple(), fill_value=value.__int__(), dtype=torch.int),)
    elif isinstance(value, ir.DenseIntElementsAttr):
        if value.is_splat:
            return (
                torch.full(
                    size=tuple(value.type.shape),
                    fill_value=value.get_splat_value().value,
                    dtype=benchgc.util.get_dtype(str(value.get_splat_value().type)),
                ),
            )
        else:
            raise Exception("only support splat value now")
    else:
        raise Exception("Not support constant type %s", type(value))


def ref_mulf(
    cache: MLIRCache, op: ir.OpView, var: Dict[str, torch.Tensor]
) -> Tuple[torch.Tensor, ...]:
    return (var[cache.opr[0]] * var[cache.opr[1]],)


def ref_addf(
    cache: MLIRCache, op: ir.OpView, var: Dict[str, torch.Tensor]
) -> Tuple[torch.Tensor, ...]:
    return (var[cache.opr[0]] + var[cache.opr[1]],)


def ref_maxf(
    cache: MLIRCache, op: ir.OpView, var: Dict[str, torch.Tensor]
) -> Tuple[torch.Tensor, ...]:
    return (torch.max(var[cache.opr[0]], var[cache.opr[1]]),)


def ref_minf(
    cache: MLIRCache, op: ir.OpView, var: Dict[str, torch.Tensor]
) -> Tuple[torch.Tensor, ...]:
    return (torch.min(var[cache.opr[0]], var[cache.opr[1]]),)


def ref_muli(
    cache: MLIRCache, op: ir.OpView, var: Dict[str, torch.Tensor]
) -> Tuple[torch.Tensor, ...]:
    return (var[cache.opr[0]] * var[cache.opr[1]],)


def ref_addi(
    cache: MLIRCache, op: ir.OpView, var: Dict[str, torch.Tensor]
) -> Tuple[torch.Tensor, ...]:
    return (var[cache.opr[0]] + var[cache.opr[1]],)


def ref_maxsi(
    cache: MLIRCache, op: ir.OpView, var: Dict[str, torch.Tensor]
) -> Tuple[torch.Tensor, ...]:
    return (torch.max(var[cache.opr[0]], var[cache.opr[1]]),)


def ref_minsi(
    cache: MLIRCache, op: ir.OpView, var: Dict[str, torch.Tensor]
) -> Tuple[torch.Tensor, ...]:
    return (torch.min(var[cache.opr[0]], var[cache.opr[1]]),)
