#!/usr/bin/env python3
# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

# pyre-strict

from typing import List, Optional

from fbpcs.infra.certificate.certificate_provider import CertificateProvider

from fbpcs.private_computation.entity.private_computation_instance import (
    PrivateComputationInstance,
    PrivateComputationInstanceStatus,
)
from fbpcs.private_computation.service.private_computation_stage_service import (
    PrivateComputationStageService,
)


class DummyStageService(PrivateComputationStageService):
    """
    Stage service that does nothing. It is used in stage flows as a dummy node akin
    to those found in linked list implementions. Having a DummyStageService in the flow
    reduces the need for special logic

    Per some online wisdom:
    A dummy node is a node that will not contain any usable value but will always carry the location of the front of the list.
    """

    async def run_async(
        self,
        pc_instance: PrivateComputationInstance,
        server_certificate_provider: CertificateProvider,
        ca_certificate_provider: CertificateProvider,
        server_certificate_path: str,
        ca_certificate_path: str,
        server_ips: Optional[List[str]] = None,
    ) -> PrivateComputationInstance:
        """
        Does nothing except return pc_instance back to caller
        """
        return pc_instance

    def get_status(
        self,
        pc_instance: PrivateComputationInstance,
    ) -> PrivateComputationInstanceStatus:
        """
        Does nothing except return pc_instance.status back to caller
        """
        return pc_instance.infra_config.status
