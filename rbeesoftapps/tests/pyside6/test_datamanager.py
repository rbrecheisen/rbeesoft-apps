import os
from rbeesoftapps.pyside6.common.data.datamanager import DataManager


def test_datamanager():
    manager = DataManager()
    file = manager.load_file(os.path.abspath('tests/data/file.txt'))
    assert file
    assert file.id()
    assert file.name() == 'file.txt'
    assert file.path() == os.path.abspath('tests/data/file.txt')
    fileset = manager.load_fileset(os.path.abspath('tests/data'))
    assert fileset
    assert fileset.id()
    assert fileset.name() == 'data'
    assert fileset.path() == os.path.abspath('tests/data')
    dicom_file = manager.load_dicom_file(os.path.abspath('tests/data/dicomfile.dcm'))
    assert dicom_file.id()
    assert dicom_file.name() == 'dicomfile.dcm'
    assert dicom_file.path() == os.path.abspath('tests/data/dicomfile.dcm')
    dicom_file = manager.load_dicom_file(os.path.abspath('tests/data/file.txt'))
    assert dicom_file.id() is None
    try:
        # This should fail because DICOM files have different series instance UIDs
        manager.load_dicom_series(os.path.abspath('tests/data'))
        assert False
    except ValueError:
        pass
    dicom_series = manager.load_dicom_series(os.path.abspath('tests/data/series'))
    assert dicom_series
    assert dicom_series.id()
    assert dicom_series.name() == 'series'
    assert dicom_series.path() == os.path.abspath('tests/data/series')