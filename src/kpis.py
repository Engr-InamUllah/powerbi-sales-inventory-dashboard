import csv
from datetime import date

def build_inventory_kpis(sales_path,inventory_path):
 sales=list(csv.DictReader(open(sales_path,encoding="utf-8"))); inventory=list(csv.DictReader(open(inventory_path,encoding="utf-8")))
 sold={}
 for r in sales:sold[r["product_id"]]=sold.get(r["product_id"],0)+int(r["quantity"])
 return [{"product_id":r["product_id"],"on_hand":int(r["on_hand"]),"units_sold":sold.get(r["product_id"],0),"sell_through":round(sold.get(r["product_id"],0)/max(int(r["on_hand"])+sold.get(r["product_id"],0),1),4)} for r in inventory]