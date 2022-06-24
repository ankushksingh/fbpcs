# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

# pyre-strict

import unittest
from unittest.mock import mock_open, patch

from fbpcs.infra.logging_service.download_logs.utils.utils import Utils


class TestUtils(unittest.TestCase):
    def setUp(self) -> None:
        self.utils = Utils()

    def test_create_file(self) -> None:

        fake_file_path = "fake/file/path"
        content_list = ["This is test string"]
        with patch(
            "fbpcs.infra.logging_service.download_logs.utils.utils.open",
            mock_open(),
        ) as mocked_file:
            with self.subTest("basic"):
                self.utils.create_file(
                    file_location=fake_file_path, content=content_list
                )
                mocked_file.assert_called_once_with(fake_file_path, "w")
                mocked_file().write.assert_called_once_with(content_list[0] + "\n")

            with self.subTest("ExceptionOpen"):
                mocked_file.side_effect = IOError()
                with self.assertRaisesRegex(Exception, "Failed to create file*"):
                    self.utils.create_file(
                        file_location=fake_file_path, content=content_list
                    )

    def test_write_to_file(self) -> None:
        pass

    def test_create_folder(self) -> None:
        pass

    def test_compress_downloaded_logs(self) -> None:
        pass

    def test_copy_file(self) -> None:
        pass
