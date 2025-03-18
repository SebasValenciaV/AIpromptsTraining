from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Mejores prompts
    best_prompts = {
        "Tecnología y Software": [
            "Explica los conceptos básicos de Python a través de ejemplos claros y prácticos.",
            "Escribe un tutorial paso a paso para crear una aplicación web simple con JavaScript y Node.js.",
            "Compara y contrasta TypeScript con JavaScript, proporcionando casos de uso donde cada uno es más beneficioso.",
            "¿Cómo optimizar un algoritmo de búsqueda binaria para grandes conjuntos de datos?",
            "Elabora una guía detallada para depurar errores comunes en aplicaciones React.",
            "Describe las mejores prácticas para gestionar el estado global en una aplicación Angular.",
            "Predice las tendencias más importantes en inteligencia artificial para los próximos cinco años.",
            "Analiza cómo la computación cuántica podría cambiar la criptografía moderna.",
            "Cómo la implementación de DevOps puede mejorar el ciclo de desarrollo de software."
        ],
        "Vida Real y Cotidiana": [
            "Crea un plan de ejercicios semanales para mejorar la salud cardiovascular.",
            "Sugerir recetas de cocina sencillas y saludables para una semana.",
            "Consejos para mantener un equilibrio saludable entre el trabajo y la vida personal.",
            "Guía paso a paso para mejorar las habilidades de comunicación en el trabajo.",
            "Describe un método efectivo para establecer y cumplir metas personales a corto plazo.",
            "Comparte estrategias para manejar el estrés en situaciones de alta presión.",
            "Lista de gadgets tecnológicos imprescindibles para hacer las tareas del hogar más fáciles.",
            "Elabora un plan de organización mensual para mantener el hogar libre de desorden.",
            "¿Cómo utilizar aplicaciones móviles para mejorar la gestión del tiempo a diario?"
        ]
    }

    # Malos prompts
    bad_prompts = {
        "Tecnología y Software": [
            "Dime algo sobre C++.",
            "Cómo funciona Java.",
            "¿Qué es un programa?",
            "Cómo solucionar un error.",
            "Resuelve mi problema en Java.",
            "Arregla mi computadora.",
            "Habla sobre tecnología.",
            "Explícale tecnología a un niño.",
            "Cuéntame algo sobre computadoras."
        ],
        "Vida Real y Cotidiana": [
            "Dame consejos saludables.",
            "¿Qué es el fitness?",
            "Cómo ser saludable.",
            "Cómo ser mejor.",
            "Dime algo sobre desarrollo personal.",
            "Hazme feliz.",
            "Ayúdame a organizarme.",
            "Qué puedo hacer hoy.",
            "Dame un consejo."
        ]
    }

    return render_template('index.html', best_prompts=best_prompts, bad_prompts=bad_prompts)

@app.route('/auditoria')
def auditoria():
    # Ejemplos de respuestas de IA con código
    correct_responses = [
        {
            "prompt": "Escribe una función en Python que sume dos números y muestre el resultado.",
            "response": "Aquí tienes una función simple en Python:",
            "code": """def sumar(a, b):
    return a + b

resultado = sumar(3, 5)
print(f"El resultado es: {resultado}")""",
            "execution": "El resultado es: 8"
        },
        {
            "prompt": "Crea un objeto JSON para representar un usuario con nombre, edad y correo electrónico.",
            "response": "Aquí tienes un ejemplo de un objeto JSON:",
            "code": '{\n  "nombre": "Juan",\n  "edad": 30,\n  "correo": "juan@example.com"\n}',
            "execution": "JSON válido"
        }
    ]

    incorrect_responses = [
        {
            "prompt": "Escribe una función en Python que sume dos números y muestre el resultado.",
            "response": "Aquí hay un error en la función:",
            "code": """def sumar(a, b):
    return a - b  # Error: debería ser a + b

resultado = sumar(3, 5)
print(f"El resultado es: {resultado}")""",
            "execution": "El resultado es: -2"
        },
        {
            "prompt": "Crea un objeto JSON para representar un usuario con nombre, edad y correo electrónico.",
            "response": "Aquí hay un error en el JSON:",
            "code": '{\n  "nombre": "Juan",\n  "edad": "treinta",\n  "correo": "juan@example.com"\n}',  # Error: edad debería ser un número
            "execution": "JSON inválido"
        }
    ]

    return render_template('auditoria.html', correct_responses=correct_responses, incorrect_responses=incorrect_responses)

if __name__ == '__main__':
    app.run(debug=True)