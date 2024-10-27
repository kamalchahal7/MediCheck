import os

from flask_cors import CORS
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from openai import OpenAI

client = OpenAI (
    api_key = os.getenv('chat_api_key')
)

from datetime import datetime
import pytz



def fetch(label):
    if label == "No Tumour":
        description = "The MRI scan reveals no signs of tumors or abnormal growths in the brain. The images demonstrate a healthy and normal structure of the brain, with no indications of masses, lesions, or other irregularities that could suggest the presence of a tumor. The surrounding brain tissue appears intact, and there are no abnormalities in the ventricles, which are the fluid-filled cavities of the brain. Additionally, there is no evidence of edema or swelling that may indicate any underlying pathology. These results are reassuring and suggest that the brain is functioning properly without any tumors or significant issues that would require further intervention."
    elif label == "Glioma":
        description = "Gliomas are tumors that originate in glial cells, which support neurons, and can include types such as astrocytomas, oligodendrogliomas, and ependymomas. Common symptoms include headaches, seizures, cognitive changes, and neurological deficits. The causes of gliomas can be linked to genetic factors like inherited syndromes (e.g., neurofibromatosis), environmental exposures to chemicals and radiation, and demographic factors, with a higher prevalence in adults aged 45-70, particularly in males. Gliomas grow by invading surrounding tissues, making complete surgical removal challenging, and are graded from I (slow-growing, benign) to IV (glioblastoma, aggressive), with higher grades indicating more rapid growth. Treatment approaches typically involve surgery to remove as much of the tumor as possible, radiation therapy to kill remaining cells, chemotherapy with drugs like temozolomide, targeted therapy focusing on specific genetic mutations, and participation in clinical trials for experimental treatments. Prognosis varies by tumor type, grade, and patient health, with lower-grade gliomas generally offering better outcomes than high-grade glioblastomas, which are more aggressive."
    elif label == "Pituitary":
        description = "Pituitary tumors are abnormal growths that develop in the pituitary gland, a small gland located at the base of the brain that regulates various hormonal functions in the body. These tumors can be classified as functional, producing excess hormones that lead to various disorders such as Cushing's disease (excess cortisol), acromegaly (excess growth hormone), or hyperprolactinemia (excess prolactin), or non-functional, which do not produce hormones but may cause symptoms due to their size or pressure on surrounding structures. The exact cause of pituitary tumors remains unclear, although genetic factors and certain syndromes like Multiple Endocrine Neoplasia (MEN) are linked to their development. Symptoms may include headaches, vision problems, and hormonal imbalances, depending on the tumor's size and type. Diagnosis typically involves imaging studies, such as MRI, along with hormone level assessments. Treatment options include surgery to remove the tumor, radiation therapy, and medication to manage hormone production, with the choice depending on the tumor's characteristics and the patient's overall health. Prognosis varies based on tumor type and size, with many patients experiencing significant improvement after treatment."
    elif label == "Meningioma":
        description = "Meningiomas are tumors that arise from the meninges, the protective membranes covering the brain and spinal cord, and are typically classified as benign (grade I) or atypical (grade II) with some being malignant (grade III). Common symptoms include headaches, seizures, and neurological deficits, often depending on the tumor's size and location. The exact cause of meningiomas is not well understood, though risk factors may include genetic predispositions, such as neurofibromatosis type II, exposure to radiation, and being female, as they are more prevalent in women. Meningiomas tend to grow slowly and can be well-defined, making surgical removal often successful, but they can recur. Treatment typically involves surgical resection, which is the primary approach, followed by radiation therapy for atypical or unresectable tumors. In cases where surgery is not possible, or if the tumor is asymptomatic and small, careful observation may be recommended. Prognosis is generally favorable for benign meningiomas, with a high rate of long-term survival, but malignant types have a poorer outlook."
    
    return description
