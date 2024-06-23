
import re
from pydantic import BaseModel
from farpenpy.subreports import SubReport
from typing import List


class ApportionmentItem(BaseModel):
    codigo: str
    cns: str
    nome: str
    comarca: str
    valor1_proprios: str
    valor2_comp: str
    valor3_receb: str
    valor4_total_atos: str
    valor5_rateio: str
    valor6_total_rat: str
    valor7_outros: str
    valor8_sub_total: str
    valor9_compl: str
    valor10_proj_cid: str
    qtds_pc: str
    valor11_total: str
    valor12_atos_pagos: str
    valor13_rend_totais: str


class ApportionmentSubReport(SubReport):
    def __init__(self) -> None:
        super().__init__()
        self._regex_apportionment = r"(?i)^(?P<codigo>\d+) " \
                                    r"+(?P<cns>\d+) +(?P<nome>RCPN  ([-'0-9a-zÀ-ÿ]+?\s{1})+)\s{2,}(?P<comarca>([-'0-9a-zÀ-ÿ]+?\s{1})+)\s{2,}" \
                                    r"R\$ (?P<valor1_proprios>[0-9.,]+) +R\$ (?P<valor2_comp>[0-9.,]+) +R\$ (?P<valor3_receb>[0-9.,]+) " \
                                    r"+R\$ (?P<valor4_total_atos>[0-9.,]+) +R\$ (?P<valor5_rateio>[0-9.,]+) +R\$ (?P<valor6_total_rat>[0-9.,]+) " \
                                    r"+R\$ (?P<valor7_outros>[0-9.,]+) +R\$ (?P<valor8_sub_total>[0-9.,]+) +R\$ (?P<valor9_compl>[0-9.,]+) " \
                                    r"+R\$ (?P<valor10_proj_cid>[0-9.,]+) +\((?P<qtds_pc>[A-Z0-9\-]+)\) +R\$ (?P<valor11_total>[0-9.,]+) " \
                                    r"+R\$ (?P<valor12_atos_pagos>[0-9.,]+) +R\$ (?P<valor13_rend_totais>[0-9.,]+)$"

    def trigger(self, page_data) -> bool:
        return page_data[0].endswith("Relatório de Rateio")

    def handler(self, page_data) -> List[ApportionmentItem]:
        found_data = []
        
        for line in page_data:
            
            match = re.match(self._regex_apportionment, line)
            if match:                
                found_data.append(
                    ApportionmentItem(
                        codigo=match["codigo"],
                        cns=match["cns"],
                        nome=match["nome"],
                        comarca=match["comarca"],
                        valor1_proprios=match["valor1_proprios"],
                        valor2_comp=match["valor2_comp"],
                        valor3_receb=match["valor3_receb"],
                        valor4_total_atos=match["valor4_total_atos"],
                        valor5_rateio=match["valor5_rateio"],
                        valor6_total_rat=match["valor6_total_rat"],
                        valor7_outros=match["valor7_outros"],
                        valor8_sub_total=match["valor8_sub_total"],
                        valor9_compl=match["valor9_compl"],
                        valor10_proj_cid=match["valor10_proj_cid"],
                        qtds_pc=match["qtds_pc"],
                        valor11_total=match["valor11_total"],
                        valor12_atos_pagos=match["valor12_atos_pagos"],
                        valor13_rend_totais=match["valor13_rend_totais"]
                    )
                )

        return found_data