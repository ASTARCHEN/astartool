from unittest import TestCase

import pathlib
from astartool.file.compresshelper import namelist, extractall
from astartool.file.filehelper import CalcHash


class TestCompress(TestCase):
    def setUp(self) -> None:
        base_path = pathlib.Path(__file__).parent.parent
        path = base_path / "demo_data"
        target_path = base_path / "demo_data_compress"
        target_path_part = base_path / "demo_data_compress_part"

        self.zip_path = path / "demo_compresshelper.zip"
        self.rar_path = path / "demo_compresshelper.rar"
        self.tar_path = path / "demo_compresshelper.tar"
        self.tar_bz2_path = path / "demo_compresshelper.tar.bz2"
        self.tar_gz_path = path / "demo_compresshelper.tar.gz"
        self.tar_xz_path = path / "demo_compresshelper.tar.xz"

        self.target_path = target_path
        self.target_path_part = target_path_part

    def test_extractall(self):
        extractall(self.zip_path, self.target_path / self.zip_path.name)
        extractall(self.rar_path, self.target_path / self.rar_path.name)
        extractall(self.tar_path, self.target_path / self.tar_path.name)
        extractall(self.tar_bz2_path, self.target_path / self.tar_bz2_path.name)
        extractall(self.tar_gz_path, self.target_path / self.tar_gz_path.name)
        extractall(self.tar_xz_path, self.target_path / self.tar_xz_path.name)
        p1, p2, p3, p4, p5, p6 = self.target_path / self.zip_path.name, self.target_path / self.rar_path.name, \
                                 self.target_path / self.tar_path.name, self.target_path / self.tar_bz2_path.name, self.target_path / self.tar_gz_path.name, \
                                 self.target_path / self.tar_xz_path.name
        for a, b, c, d, e, f in zip(p1.rglob("*.*"), p2.rglob("*.*"), p3.rglob("*.*"), p4.rglob("*.*"), p5.rglob("*.*"), p6.rglob("*.*")):
            ha = CalcHash(a)
            hb = CalcHash(b)
            hc = CalcHash(c)
            hd = CalcHash(d)
            he = CalcHash(e)
            hf = CalcHash(f)
            self.assertEqual(ha, hb)
            self.assertEqual(ha, hc)
            self.assertEqual(ha, hd)
            self.assertEqual(ha, he)
            self.assertEqual(ha, hf)

    def test_extractall_part(self):
        extractall(self.zip_path, self.target_path_part / self.zip_path.name, ["demo_data/test_namelist.py"])
        extractall(self.rar_path, self.target_path_part / self.rar_path.name, ["demo_data/test_namelist.py"])
        extractall(self.tar_path, self.target_path_part / self.tar_path.name, ["demo_data/test_namelist.py"])
        extractall(self.tar_bz2_path, self.target_path_part / self.tar_bz2_path.name, ["demo_data/test_namelist.py"])
        extractall(self.tar_gz_path, self.target_path_part / self.tar_gz_path.name, ["demo_data/test_namelist.py"])
        extractall(self.tar_xz_path, self.target_path_part / self.tar_xz_path.name, ["demo_data/test_namelist.py"])
        p1, p2, p3, p4, p5, p6 = self.target_path_part / self.zip_path.name, self.target_path_part / self.rar_path.name, \
                                 self.target_path_part / self.tar_path.name, self.target_path_part / self.tar_bz2_path.name, self.target_path_part / self.tar_gz_path.name, \
                                 self.target_path_part / self.tar_xz_path.name
        for a, b, c, d, e, f in zip(p1.rglob("*.*"), p2.rglob("*.*"), p3.rglob("*.*"), p4.rglob("*.*"), p5.rglob("*.*"), p6.rglob("*.*")):
            ha = CalcHash(a)
            hb = CalcHash(b)
            hc = CalcHash(c)
            hd = CalcHash(d)
            he = CalcHash(e)
            hf = CalcHash(f)
            self.assertEqual(ha, hb)
            self.assertEqual(ha, hc)
            self.assertEqual(ha, hd)
            self.assertEqual(ha, he)
            self.assertEqual(ha, hf)
