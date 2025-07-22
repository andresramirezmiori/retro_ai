🧠 RetroIA – Retrospectivas asistidas con agentes de IA

RetroIA es una herramienta para facilitar retrospectivas de equipo asistidas por inteligencia artificial. Pensado para equipos distribuidos, propone una nueva forma de hacer retrospectivas: más personal, más asincrónica y completamente mediada por asistentes virtuales.

> 🌟 El objetivo no es reemplazar la dinámica humana, sino hacerla más fluida, inclusiva y automatizable.




---

🚀 ¿Qué hace diferente a RetroIA?

Cada participante interactúa con su propio agente IA (TerapIA), que lo guía y ayuda a registrar sus ideas.

Un agente especial (RetroGuía) asiste al administrador en la facilitación: apertura, tiempos, resúmenes, y generación de acciones.

La interfaz es mínima: casi todo ocurre por chat, sin necesidad de botones ni formularios.

Todo queda guardado: los ítems, las conversaciones, los comentarios, los action items.



---

🛠 Estado del proyecto

Este repositorio es una prueba de concepto abierta. Está en desarrollo, con foco en experimentar con ideas, agentes, herramientas y experiencia de usuario.

> Si te interesa participar, proponer ideas o ayudar, sos más que bienvenido/a 🤝




---

🔪 MVP - Primer versión funcional

¿Qué se podrá hacer?

Crear una nueva retro con nombre y descripción

Compartir un link para que el equipo se una

Que cada participante:

Interactúe con su agente IA

Cargue sus ideas en categorías: continuar, hacer distinto, dejar de hacer


Que el admin:

Inicie y cierre el tiempo de carga

Visualice todos los ítems agrupados

Comente, edite y genere action items

Pida un resumen automático




---

🧱 Tecnologías

Backend: FastAPI + WebSockets

Base de datos: SQLite (por ahora)

Agentes: pydantic-ai

Frontend: HTML + jQuery minimal (sin framework por ahora)



---

📆 Modelo de datos

El sistema incluye las siguientes entidades:

Retro: instancia de retrospectiva

Participant: usuario dentro de una retro

RetroItem: idea registrada (continuar / mejorar / dejar)

Conversation y Message: historial de chat con el agente

ActionItem: acciones derivadas de ítems

Comment: observaciones del admin


El DER completo está disponible en la carpeta docs.


---

✨ Próximas ideas y mejoras

Exportar resultados (PDF, Markdown)

Asignación de action items con deadlines

Reutilizar columnas personalizadas

Ranking por votos o etiquetas

Interfaz alternativa estilo terminal (panel inferior)

Autenticación o integración con Slack/Meet



---

🧪 Cómo correrlo

A completar cuando esté el primer código disponible.


---

🧠 Créditos

Este proyecto fue creado por Andrés, como exploración abierta para experimentar con agentes y retros inteligentes.


---

📜 Licencia

MIT

