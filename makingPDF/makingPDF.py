from reportlab.pdfgen import canvas

def GeranddoPDF(lista):
    try:
        nome_PDF= input('Informe o nome do PDF: ')
        pdf = canvas.Canvas('{}.pdf'.format(nome_PDF))
        x = 720
        for nome,idade in lista.itens():
            x -= 20
            pdf.drawString(247,x , '{} : {}'.format(nome, idade))
        pdf.setTitle(nome_PDF)
        pdf.setFont('nome da fonte', 14)
        pdf.drawString(245,750, 'Lista de Clientes')
        pdf.setFont('nome da fonte', 11)
        pdf.drawString(245,724, 'Nome e idade')
        pdf.save()
    except:
        print('Erro ao gerar {}.pdf'.format(nome_PDF))

lista = {'Carlos': '24', 'José': '78'}

GeranddoPDF(lista)