from farpenpy import Report
from farpenpy.subreports.apportionment import ApportionmentItem
import logging


def test_load_farpen_document(caplog):
    caplog.set_level(logging.INFO)
    
    report = Report(filename="./src/report.pdf")
    available_reports = report.process()

    assert len(available_reports['ApportionmentSubReport']) > 0
    assert isinstance(available_reports['ApportionmentSubReport'][0], ApportionmentItem)
