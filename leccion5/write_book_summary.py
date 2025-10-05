import pickle
import os 

current_folder = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(current_folder, "book_summaries.pkl")
book_summaries = [
    """
        Los Pilares de la Tierra

Ambientada en la Inglaterra del siglo XII, esta novela relata el ambicioso y turbulento proceso de construcción de una majestuosa catedral gótica en el pueblo ficticio de Kingsbridge.[1][2] La trama sigue las vidas de un maestro cantero, un clérigo devoto, y la hija de un conde desterrado, entrelazando sus destinos con conspiraciones políticas, luchas de poder entre la nobleza y la Iglesia, y un período de guerra civil conocido como la anarquía inglesa.[2][3][4] Es un retrato detallado y apasionante de la vida medieval, el arte de la arquitectura y la resiliencia del espíritu humano.
        """,
    """
        De animales a dioses

Esta obra de divulgación histórica traza un vertiginoso recorrido por los 300.000 años de la historia de la humanidad.[5][6] El autor examina cómo el Homo sapiens, una especie de simios insignificantes, llegó a dominar el planeta.[6] Su argumento principal es que el éxito de nuestra especie se debe a nuestra capacidad única de creer en ficciones o "mitos colectivos", como las religiones, las naciones, los derechos humanos o el dinero, lo que nos permite cooperar de forma flexible en grandes números.[6][7][8] El libro explora las revoluciones clave, como la cognitiva, la agrícola y la científica, para revelar por qué somos como somos hoy.[7]
""",
    """
    Ana Karenina

Esta extensa novela rusa es considerada una cumbre del realismo literario y una de las obras más importantes del siglo XIX. Se centra en dos historias de amor contrastantes: la apasionada y destructiva relación adúltera de Ana Karenina con el joven y apuesto conde Vronsky, y el cortejo y matrimonio feliz del terrateniente Levin con Kitty Shtcherbatsky. A través de estas vidas, el libro ofrece una profunda crítica a la hipocresía de la sociedad aristocrática rusa de la época y aborda temas universales como el amor, la familia, la fe, la política y la búsqueda del sentido de la vida.
    """,
    """
    1984

Ambientada en un futuro totalitario dominado por el Partido Único y su líder omnipresente, el Gran Hermano, esta novela presenta una sociedad donde cada movimiento de los ciudadanos es vigilado por la Policía del Pensamiento.[1] La historia sigue a Winston Smith, un funcionario que, harto de la constante vigilancia y la manipulación de la historia, comienza a desafiar al sistema en su búsqueda de la verdad y la libertad individual. Es una de las distopías más influyentes, que introdujo conceptos como la neolengua (un lenguaje para reducir el pensamiento) y la constante reescritura del pasado.[1]
    """,
    """
     La Paciente Silenciosa

Un thriller psicológico sobre Alicia Berenson, una famosa pintora cuya vida da un giro macabro cuando asesina a su marido de cinco disparos y, desde ese momento, se niega a pronunciar una sola palabra. Su mutismo la convierte en un enigma para el público y en el centro de atención de una unidad de seguridad. Theo Faber, un psicoterapeuta forense con una obsesión por el caso, está convencido de que puede hacerla hablar, y se adentra en el misterio para desentrañar la verdad detrás del silencio, revelando secretos oscuros que lo llevarán a un final completamente inesperado.
    """,
    """
    Cambios pequeños, resultados extraordinarios

Este libro se centra en la importancia de los pequeños cambios diarios, o "hábitos atómicos", para lograr transformaciones significativas en la vida personal y profesional. El autor profundiza en la psicología detrás de los hábitos, ofreciendo un marco práctico de cuatro sencillos pasos (hacerlo obvio, atractivo, sencillo y satisfactorio) para formar nuevas rutinas positivas, mantenerlas a largo plazo y superar los obstáculos que impiden el crecimiento personal. Es una guía práctica para construir un sistema que te permita mejorar constantemente.
    """,
    """
    Maus: Relato de un superviviente

Una obra fundamental, y la primera novela gráfica en ganar un premio Pulitzer, donde el autor narra la historia real de su padre, Vladek Spiegelman, un judío polaco superviviente del Holocausto. La narración es una biografía conmovedora donde los judíos son representados como ratones y los nazis como gatos, utilizando la metáfora animal para contar la crudeza de la Shoá y, simultáneamente, explorar la compleja relación entre un hijo y un padre marcado por el trauma.
    """,
    """
    Te Quiero

Tras la trágica muerte de su esposo, Holly se encuentra sumida en el dolor. Justo cuando intenta reconstruir su vida, recibe un misterioso paquete que contiene una serie de cartas.[6] Su marido, antes de morir, le había dejado estas cartas, cada una con una instrucción, un mensaje o un desafío, para ayudarla a superar el luto y animarla a seguir adelante con una nueva vida sin él.[6] La emotiva historia gira en torno al amor perdurable y el camino de la protagonista para redescubrirse a sí misma.
    """,
    """
    l Principito

Una obra atemporal que, aunque se presenta como un cuento infantil, está dirigida a lectores de todas las edades. Un aviador que se estrella en el desierto conoce a un pequeño príncipe llegado de un asteroide lejano, el B-612. A través de las conversaciones con el Principito y los peculiares personajes que encuentra en su viaje por diversos planetas (el rey, el vanidoso, el bebedor), la obra reflexiona sobre temas profundos como la amistad, el amor, la pérdida, el sentido de la vida, la soledad y la verdadera esencia de lo que es importante.
    """,
    """
    Cuarenta y tres maneras de soltarse el pelo

Este poemario de una de las voces más aclamadas de la poesía moderna explora el universo de las emociones humanas en el contexto de la sociedad actual. Los versos abordan temas de amor, dependencia emocional, la búsqueda de la identidad y el autocuidado.[2] Es una obra íntima y accesible, que utiliza un lenguaje directo y sincero para conectar con las experiencias cotidianas del lector, invitándole a soltar las ataduras emocionales y a abrazar el yo interior.
Sources help
    """,
    """
    La Mujer del Viajero en el Tiempo

Esta novela es una emotiva y compleja historia de amor centrada en el matrimonio de Henry DeTamble, un bibliotecario con un raro desorden genético que lo obliga a viajar involuntariamente a través del tiempo, y Clare Abshire, la artista que lo ama. El viaje de Henry es caótico: aparece y desaparece en momentos y lugares aleatorios, desnudo y sin control sobre su destino.

La trama se desarrolla de forma no lineal. Clare conoce a un Henry de 40 años cuando ella es una niña, y lo encuentra a lo largo de su vida en orden cronológico, mientras que Henry conoce a Clare en un orden totalmente desordenado. La historia explora la belleza y la frustración de un amor que desafía las leyes de la física, el trauma de las constantes separaciones y el profundo impacto de saber de antemano lo que el tiempo depara.
    """,
]


with open(output_path, "wb") as file:
    pickle.dump(book_summaries, file)
