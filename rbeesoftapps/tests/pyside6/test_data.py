import os
from rbeesoftapps.pyside6.core.data.dicomfile import DicomFile
from rbeesoftapps.pyside6.core.data.dicomseries import DicomSeries


def test_data():

    dicom_file = DicomFile(os.path.abspath('tests/data/dicomfile.dcm'))
    assert dicom_file.load()
    assert dicom_file.data()
    assert dicom_file.path() == os.path.abspath('tests/data/dicomfile.dcm')

    dicom_file = DicomFile(os.path.abspath('tests/data/file.txt'))
    assert not dicom_file.load()

    dicom_series = DicomSeries(os.path.abspath('tests/data'))
    try:
        # This should not work because of mismatching series instance UIDs
        dicom_series.load()
        assert False
    except ValueError:
        assert True

    dicom_series = DicomSeries(os.path.abspath('tests/data/series'))
    assert dicom_series.load()
    assert dicom_series.path() == os.path.abspath('tests/data/series')
    assert len(dicom_series.files()) == 2