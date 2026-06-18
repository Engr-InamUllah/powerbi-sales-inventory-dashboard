import tempfile,unittest
from pathlib import Path
from src.kpis import build_inventory_kpis
class TestKPI(unittest.TestCase):
 def test_sell_through(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d);(p/"s.csv").write_text("product_id,quantity\nP1,5\n");(p/"i.csv").write_text("product_id,on_hand\nP1,5\n")
   self.assertEqual(build_inventory_kpis(p/"s.csv",p/"i.csv")[0]["sell_through"],.5)
if __name__=="__main__":unittest.main()