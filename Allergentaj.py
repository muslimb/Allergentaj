from Bio.SeqIO import parse

b = input('Please select the interface language,\n'
          'if you want to conduct the analysis\n'
          'in English, enter the letter "E", if\n'
          'in Russian, enter the letter "R".\n'
          'For more information about the program,\n'
          'enter the letter "H".\n'
          'Пожалуйста, выберите язык интерфейса,\n'
          'если вы хотите провести анализ на английском,\n'
          'введите букву "E", если на русском, введите\n'
          'букву "R". Для получения подробной информации\n'
          'о программе введите букву "H".\n'
          'Enter/Введите: ')

if b == 'E':
    print('Before starting the program,\n'
          'install the BioPython package.\n'
          '(https://biopython.org/)!\n')
    print('-------------------------------------------------------')

    a = input('Enter the amino acid sequence in capital letters: ')
    print('-------------------------------------------------------')
    c = input('Specify the path to the file that contains\n'
          'the amino acid sequences of human allergens\n'
          '(in fasta format). You can download the\n'
          'allergentaj collection of human allergens\n'
          'available to users by following the link\n'
          'https://github.com/muslimb/Allergen-protein-dataset.\n'
          'You can also insert the analyzed amino acid\n'
          'sequence into the repository and use it in your\n'
          'research: ')

    file = open(c)
    records = parse(file, 'fasta')
    m = list()
    n = list()

    for seq_record1 in records:
        y = seq_record1.seq
        if a in y:
            print('Your amino acid sequence is contained in the following proteins: ')
            print(seq_record1.description)
            m.append(seq_record1.description)
        elif a not in seq_record1:
            n.append(seq_record1.description)
    print('The amino acid sequence you indicated is contained\n'
          'in', len(m), 'human allergen proteins.')
    print('---------------------------------------------------------')
    print('The amino acid sequence you specified is not contained\n'
          'in', len(n), 'human allergen proteins')
    print('---------------------------------------------------------')
    print('For more information about human allergens,\n'
          'enter the allergen identification number\n'
          'into the UniProt (https://www.uniprot.org/)\n'
          'or NCBI (https://www.ncbi.nlm.nih.gov/) database.')

elif b == 'R':
    print('Перед запуском программы\n'
          'установите пакет BioPython.\n'
          'https://biopython.org/!')
    print('--------------------------------------------------------------------')

    a = input('Введите аминокислотную последовательность\n'
              'заглавными буквами: ')
    c = input('Укажите путь к файлу который содержит\n'
          'аминокислотные последовательности\n'
          'аллергенов человека (в формате фаста).\n'
          'Вы можете скачать доступную для\n'
          'пользователей allergentaj коллекцию\n'
          'аллергенов человека по ссылке\n'
          'https://github.com/muslimb/Allergen-protein-dataset.\n'
          'Также вы можете вставить анализируемую\n'
          'аминокислотную последовательность в\n'
          'репазиторий и использовать ее в своих\n'
          'исследованиях: ')

    file = open(c)
    records = parse(file, 'fasta')
    m = list()
    n = list()

    for seq_record1 in records:
        y = seq_record1.seq
        if a in y:
            print('Ваша аминокислотная последовательность содержится в составе следующих белков: ')
            print(seq_record1.description)
            m.append(seq_record1.description)
        elif a not in seq_record1:
            n.append(seq_record1.description)
    print('------------------------------------------------------')
    print('Указанная вами аминокислотная последовательность\n'
          'содержится в', len(m), 'белках аллергенах\n'
          'человека.\n')
    print('------------------------------------------------------')
    print('Указанная вами аминокислотная последовательность\n'
          'не содержится в', len(n), 'белках аллергенах\n'
          'человека.\n')
    print('------------------------------------------------------')
    print('Для получения дополнительной информации об\n'
          'аллергенах человека введите идентификационный\n'
          'номер аллергена в базу данных UniProt\n'
          '(https://www.uniprot.org/) или NCBI\n'
          '(https://www.ncbi.nlm.nih.gov/).')

elif b == 'H':
    print('The program is designed to identify overlapping amino\n'
          'acid sequences of proteins of the human body and foreign\n'
          'proteins acting as allergens. The program is bundled\n'
          'with the original file (allergen.fasta), which contains\n'
          'amino acid sequences of 2427 proteins capable of causing\n'
          'an allergic reaction in humans. Access to the program can\n'
          'be obtained on the Github website (https://github.com/muslimb/Allergentaj.git).\n'
          'At the input, the program accepts the amino acid sequence\n'
          'of the peptide of interest, after which it aligns the amino\n'
          'acid sequences of the peptide with the amino acid sequences of human\n'
          'allergens. At the output, the program returns allergen data\n'
          '(ID number, organism, protein, etc.) that contain\n'
          'overlapping amino acid sequences with the analyzed protein.\n'
          'The program is useful for assessing the risk of an allergic\n'
          'reaction in humans after vaccination or viral infection due\n'
          'to molecular mimicry between human autoantigens and antigens\n'
          'of viruses or viral vaccines, and can also be used in\n'
          'preventive allergology to assess the allergenicity of\n'
          'protein preparations and food proteins.\n'
          '---------------------------------------------------------------\n'
          'Программа предназначена для выявления перекрывающихся\n'
          'аминокислотных последовательностей белков организма\n'
          'человека и чужеродных белков выступающих в качестве аллергенов.\n'
          'Программа работает в комплекте с оригинальным файлом\n'
          '(allergen.fasta) в котором содержатся аминокислотные\n'
          'последовательности 2427 белков способных вызывать\n'
          'аллергическую реакцию у человека. Доступ к программе можно\n'
          'получить на сайте Github (https://github.com/muslimb/Allergentaj.git).\n'
          'На вход программа принимает аминокислотную последовательность\n' 
          'интересующего пептида, после чего выравнивает аминокислотные\n'
          'последовательности пептида с аминокислотными последовательностями\n'
          'аллергенов человека. На выходе программа возвращает\n'
          'данные аллергенов (ID номер, организм, белок и др.)\n'
          'которые содержат перекрывающиеся аминокислотные последовательности\n'
          'с анализируемым белком.  Программа полезна для оценки\n'
          'риска возникновения аллергической реакции у человека\n'
          'после вакцинации или вирусной инфекции обусловленной\n'
          'молекулярной мимикрией между аутоантигенами человека и\n'
          'антигенами вирусов либо вирусных вакцин, а также может\n'
          'быть использована в превентивной аллергологии для оценки\n'
          'аллергенности белковых препаратов и пищевых белков.\n'
          '-------------------------------------------------------------------\n'
            'Author data:\n'
            'Name: Muslimbek,\n'
            'Midle name: Ghulomovich,\n'
            'Surname: Normatov,\n'
            'Contact: muslimbek_normatov@mail.ru\n'
          '-------------------------------------------------------------------\n'
            'Данные автора:\n'
            'Имя: Муслимбек,\n'
            'Отчество: Гуломович,\n'
            'Фамиля: Норматов,\n'
            'Контакт: muslimbek_normatov@mail.ru')

elif b != 'E' and 'R' and 'h':
    print('The wrong language was entered!\n'
          'Введен неправильный язык!')