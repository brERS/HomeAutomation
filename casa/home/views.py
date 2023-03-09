from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'cards': {
            'alexa': {
                'icon': 'bi-alexa',
                'content': 'Integração com Alexa'
            },
            'raspberry': {
                'icon': 'bi-cpu',
                'content': 'Integração com Raspberry Pi'
            },
            'rele': {
                'icon': 'bi-device-ssd-fill',
                'content': 'Integração com Relé'
            },
        },
        'details': {
            'what': {
                'title': 'O que é automação residencial?',
                'content': '''
                    A automação residencial é uma tendência crescente em todo o
                    mundo, oferecendo uma experiência de casa inteligente,
                    conectada via dispositivos apropriados para tornar o dia a
                    dia mais prático e confortável.
                ''',
            },
            'how': {
                'title': 'Como fazer uma automação residencial?',
                'content': '''
                    Diversos dispositivos eletrônicos se integram de forma
                    nativa tais como lampadas inteligentes, mas também é
                    possível atraves de projeto envolvendo arduino ou
                    raspberry que permitindo o controle remoto de todos os
                    dispositivos conectados. Esses dispositivos podem ser
                    controlados por meio de um aplicativo, ou de uma assistente
                    virtual, como a Alexa.
                ''',
            },
            'benefits': {
                'title': 'Quais as vantagens da automação residencial?',
                'content': '''
                    Entre as vantagens da automação residencial estão a
                    praticidade e o conforto, pois é possível controlar todos
                    os dispositivos eletrônicos de forma remota, sem a
                    necessidade de se locomover até o local onde o dispositivo
                    está instalado.
                ''',
            },
        },
        'descriptions': {
            'alexa': {
                'background': 'alexa',
                'title': 'Alexa',
                'paragraphs': {
                    'p1': '''
                        A Alexa é um assistente virtual desenvolvido pela
                        Amazon, que pode ser integrado a diversos dispositivos
                        eletrônicos, como smartphones, tablets, caixas de som
                        e smart speakers.
                    ''',
                    'p2': '''
                        Com a integração da Alexa ao sistema de automação
                        residencial, é possível controlar a iluminação,
                        cortinas, ar-condicionado, som, câmeras de segurança e
                        outros dispositivos eletrônicos apenas com a voz, sem a
                        necessidade de usar um aplicativo ou controle remoto.
                    ''',
                    'p3': '''
                        Para utilizar a Alexa em sua automação residencial, é
                        necessário possuir dispositivos eletrônicos compatíveis
                        com a assistente virtual e configurá-los para se
                        integrarem ao sistema de automação. Além disso, é
                        possível criar rotinas personalizadas, em que a Alexa
                        executa uma série de comandos simultaneamente com
                        apenas um comando de voz.
                    ''',
                },
            },
            'raspberry': {
                'background': 'raspberrypi',
                'title': 'Raspberry Pi',
                'paragraphs': {
                    'p1': '''
                        O Raspberry Pi é um computador de placa única, com
                        baixo consumo de energia e tamanho reduzido, o que
                        o torna ideal para projetos de automação residencial.
                    ''',
                    'p2': '''
                        O Raspberry Pi atua como um controlador central,
                        recebendo comandos do aplicativo e enviando sinais para
                        os dispositivos eletrônicos, permitindo o controle
                        remoto de todos os dispositivos conectados.
                    ''',
                    'p3': '''
                        Além disso, o Raspberry Pi também pode ser usado para a
                        criação de projetos personalizados de automação
                        residencial, em dispositivos como interruptores,
                        tomadas, sensores de presença e outros em que a
                        integração com a Alexa não é possível.
                    ''',
                },
            },
            'rele': {
                'background': 'rele',
                'title': 'Relé',
                'paragraphs': {
                    'p1': '''
                        Um módulo relé é uma placa eletrônica que permite o
                        controle de dispositivos elétricos por meio de sinais
                        elétricos de baixa voltagem.
                    ''',
                    'p2': '''
                        O relé é um componente eletrônico que atua como um
                        interruptor elétrico, sendo capaz de ligar e desligar
                        dispositivos que operam em alta voltagem, como
                        lâmpadas, motores e eletrodomésticos.
                    ''',
                    'p3': '''
                        Os módulos relé são utilizados em diversos projetos de
                        automação residencial e industrial, sendo uma solução
                        eficiente e segura para o controle de dispositivos
                        elétricos de alta voltagem.
                    ''',
                },
            },
        }
    }

    return render(request, 'home/pages/home.html', context)
