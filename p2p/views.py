# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.shortcuts import render

# Create your views here.
# Create your views here.
def p2p_accounting(request):
    receipt_accting=  (d for d in p2p_accting_list if (d['item_type']=='Expense' and d['accounting_entry']=='PO Receipt' ) )
    deliver_accting = (d for d in p2p_accting_list  if (d['item_type']=='Expense' and d['accounting_entry']=='PO Deliver' ) )
    invoice_accting = (d for d in p2p_accting_list if (d['accounting_entry']=='AP Invoice' ) )
    payment_accting = (d for d in p2p_accting_list  if (d['accounting_entry']=='AP Payment' ) )
     #list_accounting =  (d for d in list_accounting_expense if d['accounting_entry']=='PO Receipt' )
    return render(request, 'p2p/p2p_accounting.html',
        {'po_receipt_accting': receipt_accting, 'po_deliver_accting' : deliver_accting,
        'ap_invoice_accting':invoice_accting, 'ap_payment_accting':payment_accting})



p2p_accting_list = [
  {
    "id":1,
    "dr_cr":"DEBIT",
    "account_description":"Receiving Inventory A/c",
    "accounting_entry":"PO Receipt",
    "item_type":"Expense",
    "stream":"P2P",
    "allow_recon_accounting":0,
    "period_end_accrual":0
  },
  {
    "id":2,
    "dr_cr":"CREDIT",
    "account_description":"AP Accrual A/c",
    "accounting_entry":"PO Receipt",
    "item_type":"Expense",
    "stream":"P2P",
    "allow_recon_accounting":0,
    "period_end_accrual":0
  },
  {
    "id":3,
    "dr_cr":"DEBIT",
    "account_description":"Expense/PO Charge A/c",
    "accounting_entry":"PO Deliver",
    "item_type":"Expense",
    "stream":"P2P",
    "allow_recon_accounting":0,
    "period_end_accrual":0
  },
  {
    "id":4,
    "dr_cr":"CREDIT",
    "account_description":"Receiving Inventory A/c",
    "accounting_entry":"PO Deliver",
    "item_type":"Expense",
    "stream":"P2P",
    "allow_recon_accounting":0,
    "period_end_accrual":0
  },
  {
    "id":5,
    "dr_cr":"DEBIT",
    "account_description":"Receiving Inventory A/c",
    "accounting_entry":"PO Receipt",
    "item_type":"Inventory",
    "stream":"",
    "allow_recon_accounting":0,
    "period_end_accrual":0
  },
  {
    "id":6,
    "dr_cr":"CREDIT",
    "account_description":"AP Accrual A/c",
    "accounting_entry":"PO Receipt",
    "item_type":"Inventory",
    "stream":"",
    "allow_recon_accounting":0,
    "period_end_accrual":0
  },
  {
    "id":7,
    "dr_cr":"DEBIT",
    "account_description":"Inventory Material A/c",
    "accounting_entry":"PO Deliver",
    "item_type":"Inventory",
    "stream":"",
    "allow_recon_accounting":0,
    "period_end_accrual":0
  },
  {
    "id":8,
    "dr_cr":"CREDIT",
    "account_description":"Receiving Inventory A/c",
    "accounting_entry":"PO Deliver",
    "item_type":"Inventory",
    "stream":"",
    "allow_recon_accounting":0,
    "period_end_accrual":0
  },
  {
    "id":9,
    "dr_cr":"DEBIT",
    "account_description":"AP Accrual A/c",
    "accounting_entry":"AP Invoice",
    "item_type":"Expense / Inventory",
    "stream":"",
    "allow_recon_accounting":0,
    "period_end_accrual":0
  },
  {
    "id":10,
    "dr_cr":"CREDIT",
    "account_description":"AP Liability A/c",
    "accounting_entry":"AP Invoice",
    "item_type":"Expense / Inventory",
    "stream":"",
    "allow_recon_accounting":0,
    "period_end_accrual":0
  },
  {
    "id":11,
    "dr_cr":"DEBIT",
    "account_description":"Cash/Bank A/c",
    "accounting_entry":"AP Payment",
    "item_type":"Not Relevant",
    "stream":"",
    "allow_recon_accounting":0,
    "period_end_accrual":0
  },
  {
    "id":12,
    "dr_cr":"CREDIT",
    "account_description":"AP Liability A/c",
    "accounting_entry":"AP Payment",
    "item_type":"Not Relevant",
    "stream":"",
    "allow_recon_accounting":0,
    "period_end_accrual":0
  },
  {
    "id":13,
    "dr_cr":"DEBIT",
    "account_description":"Expense/PO Charge A/c",
    "accounting_entry":"AP Invoice",
    "item_type":"Expense",
    "stream":"",
    "allow_recon_accounting":0,
    "period_end_accrual":1
  },
  {
    "id":14,
    "dr_cr":"CREDIT",
    "account_description":"AP Liability",
    "accounting_entry":"AP Invoice",
    "item_type":"Expense",
    "stream":"",
    "allow_recon_accounting":0,
    "period_end_accrual":1
  },
  {
    "id":15,
    "dr_cr":"DEBIT",
    "account_description":"Cash/Bank A/c",
    "accounting_entry":"AP Payment Reco",
    "item_type":"Not Relevant",
    "stream":"",
    "allow_recon_accounting":1,
    "period_end_accrual":0
  },
  {
    "id":16,
    "dr_cr":"CREDIT",
    "account_description":"Cash Clearing A/c",
    "accounting_entry":"AP Payment Reco",
    "item_type":"Not Relevant",
    "stream":"",
    "allow_recon_accounting":1,
    "period_end_accrual":0
  },
  {
    "id":17,
    "dr_cr":"DEBIT",
    "account_description":"AP Liability A/c",
    "accounting_entry":"AP Payment",
    "item_type":"Not Relevant",
    "stream":"",
    "allow_recon_accounting":1,
    "period_end_accrual":0
  },
  {
    "id":18,
    "dr_cr":"CREDIT",
    "account_description":"Cash Clearing A/c",
    "accounting_entry":"AP Payment",
    "item_type":"Not Relevant",
    "stream":"",
    "allow_recon_accounting":1,
    "period_end_accrual":0
  }
]
