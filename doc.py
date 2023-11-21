from docxtpl import DocxTemplate

doc = DocxTemplate("invoice_template.docx")

invoice_list = [[2,"pen",0.5,1],
                [1,"pencil",2,3],
                [2,"book",3,6],
                [2,"pen",0.5,1],
                [1,"pencil",2,3],
                [2,"book",3,6]]

doc.render({"name":"alan","invoice_list":invoice_list })
doc.save("new_invoice.docx")