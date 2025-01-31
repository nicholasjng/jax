# Copyright 2020 The JAX Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from jax.experimental.jax2tf.jax2tf import (
  convert as convert,
  eval_polymorphic_shape as eval_polymorphic_shape,
  dtype_of_val as dtype_of_val,
  split_to_logical_devices as split_to_logical_devices,
  DisabledSafetyCheck as DisabledSafetyCheck,
  PolyShape as PolyShape
)
from jax.experimental.jax2tf.call_tf import call_tf as call_tf
# Needed by maths.qec.
from jax.experimental.jax2tf import shape_poly
