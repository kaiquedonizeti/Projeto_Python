from fpdf import FPDF

class PDF(FPDF):

    def doc_title(self, label):
        self.set_font('helvetica', 'B', size=16)
        self.cell(0, 10, label, 0, 1, 'L')
        self.ln()

    def doc_text(self, text):
        self.set_font('helvetica', '', size=12)
        self.multi_cell(0, 7, text)
        self.ln()

    def doc_img(self, img, x, y, w, h):
        self.image(img, x, y, w, h)

pdf = PDF()
pdf.add_page()

pdf.doc_title("Modalidades de Ensino em Todos os Estados do Brasil")

pdf.doc_text("O crescimento da Educação a Distância (EAD) tem sido significativo no Brasil, proporcionando maior acesso à educação para pessoas em diferentes regiões. No entanto, é importante ressaltar que a oferta de cursos pode depender da estrutura e das decisões específicas de cada instituição.")
pdf.doc_text("Os números mostraram, mais uma vez, um crescimento na educação a distância (EaD) e um recuo das matrículas presenciais em 2021.Apesar do avanço ser vantajoso para a modalidade, a EaD segue sem conquistar uma parcela do público jovem, mais afeito aos cursos presenciais ou ao modelo híbrido que mescla presencialidade com aulas remotas.")
pdf.doc_text("Mesmo assim, a educação a distância avança em quase todo o País, com destaque para o Sul, região em que as matrículas são maiores na EaD (51%) do que nos cursos presenciais (49%). Já o Norte vai na contramão, com as matrículas em cursos presenciais estão aumentando.")

pdf.ln(65)

pdf.doc_img("modalidade.png", 60, 120, 90, 70)

pdf.ln(40)

pdf.doc_title("Situação dos Cursos nos Estados do Brasil")

pdf.doc_text("É importante observar que as tendências em cursos superiores podem variar ao longo do tempo e depender de fatores como mudanças na demanda do mercado de trabalho, avanços tecnológicos, políticas educacionais e outros elementos socioeconômicos. O status de um curso pode mudar ao longo do tempo, e o que pode estar em extinção em um momento específico pode ser revitalizado ou substituído por novas áreas de estudo. ")
pdf.doc_text("Cursos em Extinção ou em Declínio:Cursos Tradicionais sem Atualização: Alguns cursos que não se adaptam às mudanças do mercado ou não incorporam avanços tecnológicos podem estar em declínio. Isso pode incluir cursos que não foram atualizados para atender às demandas contemporâneas.Áreas com Mercado de Trabalho Reduzido: Cursos que preparam profissionais para áreas com demanda decrescente no mercado de trabalho podem enfrentar desafios. Por exemplo, certas profissões manuais ou técnicas podem ser substituídas por automação.")
pdf.doc_text("Cursos Extintos ou em Processo de Extinção:Tecnologias Obsoletas: Cursos relacionados a tecnologias ou práticas que se tornaram obsoletas podem ser descontinuados. Por exemplo, cursos que ensinam programação em linguagens descontinuadas.Baixa Procura e Viabilidade Financeira: Cursos com baixa procura por parte dos estudantes e pouca viabilidade financeira para as instituições de ensino podem ser eliminados.")
pdf.doc_text("Cursos em Alta ou em Crescimento:Tecnologia da Informação e Ciência de Dados: Com o aumento da dependência da tecnologia, cursos relacionados à tecnologia da informação, ciência de dados e programação têm experimentado crescimento significativo.Sustentabilidade e Energias Renováveis: Cursos relacionados à sustentabilidade e energias renováveis têm ganhado destaque devido às preocupações ambientais e à busca por soluções mais sustentáveis.Saúde e Bem-Estar: Áreas relacionadas à saúde, como enfermagem, fisioterapia e nutrição, geralmente continuam em alta devido ao envelhecimento da população e à ênfase crescente na saúde e bem-estar.Gestão e Empreendedorismo: Cursos que preparam os alunos para cargos de gestão e empreendedorismo também têm sido valorizados, já que muitos procuram desenvolver habilidades de liderança e iniciativa empresarial.")

pdf.doc_img("situacao.png", 50, 190, 90, 70)

pdf.output("educa.pdf")