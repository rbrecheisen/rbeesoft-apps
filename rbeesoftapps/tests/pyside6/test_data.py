import os
from rbeesoftapps.pyside6.core.data.dicomfile import DicomFile
from rbeesoftapps.pyside6.core.data.dicomseries import DicomSeries
from rbeesoftapps.pyside6.core.data.dicomserieslist import DicomSeriesList


def full_path(path):
    if __name__ == '__main__':
        return os.path.abspath(f'rbeesoftapps/{path}')
    return os.path.abspath(path)


def test_data():

    dicom_file = DicomFile(full_path('tests/data/dicomfile.dcm'))
    assert dicom_file.load()
    assert dicom_file.data()
    assert dicom_file.path() == full_path('tests/data/dicomfile.dcm')

    dicom_file = DicomFile(full_path('tests/data/file.txt'))
    assert not dicom_file.load()

    dicom_series_list = DicomSeries(full_path('tests/data'))
    dicom_series_list.load()

    dicom_series_list = DicomSeries(full_path('tests/data/series'))
    assert dicom_series_list.load()
    assert dicom_series_list.path() == full_path('tests/data/series')
    assert len(dicom_series_list.files()) == 2

    dicom_series_list = DicomSeriesList('D:\\Mosamatic\\MaximeDewulf\\Patient1')
    assert dicom_series_list.load()
    dicom_series_list.print()


if __name__ == '__main__':
    test_data()