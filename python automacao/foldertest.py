from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def criar_folder_pdf():
    # Cria um arquivo PDF
    c = canvas.Canvas("folder_informativo_insulina.pdf", pagesize=letter)

    # Define o tamanho da fonte
    c.setFont("Helvetica", 12)

    # Escreve o conteúdo do folder
    c.drawString(100, 750, "Folder Informativo sobre Armazenamento e Aplicação de Insulina")
    c.drawString(100, 730, " ")
    c.drawString(100, 710, "Armazenamento Adequado:")
    c.drawString(100, 690, "- Mantenha a insulina na geladeira entre 2°C e 8°C.")
    c.drawString(100, 670, "- Não congele a insulina.")
    c.drawString(100, 650, "- Evite a exposição direta à luz solar e ao calor excessivo.")
    c.drawString(100, 630, " ")
    c.drawString(100, 610, "Aplicação da Insulina:")
    c.drawString(100, 590, "- Lave as mãos com água e sabão antes da aplicação.")
    c.drawString(100, 570, "- Escolha uma área de aplicação (abdomen, coxas, braços) e faça a limpeza com álcool.")
    c.drawString(100, 550, "- Prepare a dose conforme orientação médica e injete conforme instruído.")
    c.drawString(100, 530, " ")
    c.drawString(100, 510, "Cuidados e Precauções:")
    c.drawString(100, 490, "- Verifique regularmente o prazo de validade da insulina.")
    c.drawString(100, 470, "- Esteja ciente dos sinais de hipoglicemia e hiperglicemia.")
    c.drawString(100, 450, "- Procure assistência médica em caso de dúvidas ou problemas.")
    c.drawString(100, 430, " ")
    c.drawString(100, 410, "Contato de Emergência:")
    c.drawString(100, 390, "- Em caso de emergência, contate o seu médico ou disque 192.")

    # Salva o arquivo PDF
    c.save()

    print("Folder informativo em PDF criado com sucesso!")


# Chama a função para criar o folder em PDF
criar_folder_pdf()