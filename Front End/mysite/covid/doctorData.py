from .models import Doctor


def getAll():
    doc = []
    doc_all = Doctor.objects.all()
    for i in doc_all:
        doc.append(i.__dict__)
    return doc
