from typing import Dict, Any, List, Union
from ..utils import tty, simple_hasher, math_utils
from operator import countOf

class Squeezer:
    def __init__(self, data: List[Dict[str, Any]]) -> None:
        self.data = data
        self.data_table = {}
        self.all_tid = None


    def __make_data_table(self):
        self.data_table = {
            k: [] for k in
                list(self.data[0].keys())
        }

        for dt in self.data:
            for k, v in dt.items():
                try:
                    self.data_table[k].append(v)
                except:
                    #todo!
                    pass
    
    def __data_to_tid(self):
        fin_list = []

        for fields in self.data:
            tuple_hash = simple_hasher.hasher(
                list(fields.values())
            )
            fin_list.append(
                tty.SingleTid(
                    tuple_hash=tuple_hash,
                    fields=fields
                )
            )


        self.all_tid = tty.AllTidTty(all_tid=fin_list)
       

    def single_sim_op(ai: int, j: List[int]) -> float:
        ai / sum(j)


    def sim_cluter_tid(
        self, 
        cs: tty.ClusterStructureTty,
        sim_target: tty.SingleTidTty
    ) -> tty.SimResTty:
            make_count = lambda fn, it: math_utils.clamp(
                value=countOf(
                    self.data_table[fn], 
                    sim_target.fields[fn]
                ) - 1,
                min_val=0,
                max_val=len(self.data_table[fn]),
            )   



            tfis = {
                k: make_count(k) 
                        for k in
                            list(sim_target.fields.keys())
            }

            sch = cs.tuple_hashes
            tt = sim_target.tuple_hash





    