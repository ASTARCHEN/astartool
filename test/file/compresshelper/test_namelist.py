
from unittest import TestCase

import pathlib
from astartool.file.compresshelper import namelist


class TestCompress(TestCase):
    def setUp(self) -> None:
        base_path = pathlib.Path(__file__).parent.parent
        path = base_path / "demo_data"

        self.zip_path = path / "demo_compresshelper.zip"
        self.rar_path = path / "demo_compresshelper.rar"
        self.tar_path = path / "demo_compresshelper.tar"
        self.tar_bz2_path = path / "demo_compresshelper.tar.bz2"
        self.tar_gz_path = path / "demo_compresshelper.tar.gz"
        self.tar_xz_path = path / "demo_compresshelper.tar.xz"

    def test_namelist(self):
        namelist_zip = namelist(self.zip_path)
        namelist_rar = namelist(self.rar_path)
        namelist_tar = namelist(self.tar_path)
        namelist_tar_bz2 = namelist(self.tar_bz2_path)
        namelist_tar_gz = namelist(self.tar_gz_path)
        namelist_tar_xz = namelist(self.tar_xz_path)

        # print(namelist_tar_xz)
        self.assertCountEqual(namelist_zip, namelist_rar)
        self.assertCountEqual(namelist_zip, namelist_tar)
        self.assertCountEqual(namelist_zip, namelist_tar_bz2)
        self.assertCountEqual(namelist_zip, namelist_tar_gz)
        self.assertCountEqual(namelist_zip, namelist_tar_xz)


