# 📋 RetroIA – Lista de tareas iniciales para Codex

## ✅ Tarea 1: WebSocket por participante (chat con TerapIA)

**Objetivo:** Crear un canal WebSocket dedicado para cada participante de una retro, donde el agente TerapIA pueda interactuar con él individualmente.

**Requisitos:**
- Endpoint: `ws/retro/{retro_id}/participant/{participant_id}`
- Al conectarse, el backend debe mantener el WebSocket asociado al `participant_id` dentro del `retro_id`.
- El backend debe poder:
  - Recibir mensajes del participante
  - Simular respuesta de TerapIA
  - Enviar mensajes al participante con una función `send_to_participant()`
- Debe manejar correctamente desconexiones

> 💡 Inspirado en charla con ChatGPT sobre cómo simular rooms (como en Django Channels).

---

## ✅ Tarea 2: WebSockets por columna (broadcast de ítems)

**Objetivo:** Implementar 3 websockets por retro para recibir actualizaciones de ítems en cada columna: `"to_improve"`, `"to_stop"`, `"to_continue"`.

**Requisitos:**
- Endpoint: `ws/retro/{retro_id}/column/{column_type}`
- Todos los clientes conectados a esa columna deben recibir actualizaciones (solo lectura)
- Backend debe proveer una función:
  ```python
  async def broadcast_to_column(retro_id, column_type, item_data: dict)
  ```
- El frontend se conecta a las 3 columnas al cargar la retro

---

## ✅ Tarea 3: Render de retro desde backend

**Objetivo:** Crear una vista HTML de una retro específica que replique el diseño de `app/retro_prototype.html`.

**Requisitos:**
- Endpoint: `GET /retroia/{retro_id}`
- HTML debe incluir:
  - Nombre de la retro
  - 3 columnas (con ítems actuales de la DB)
  - Lista de participantes
  - Panel de chat (sin necesidad de que funcione aún)
- El HTML puede servirse con Jinja2 (opcional)

---

## ✅ Tarea 4: Crear retro (pantalla inicial)

**Objetivo:** Crear una retro desde una pantalla simple.

**Requisitos:**
- Endpoint: `GET /retroia/new`
  - Muestra un `input` con el nombre de la retro y botón "Crear"
- Endpoint: `POST /retroia/new`
  - Crea la retro en la base
  - Redirige a `/retroia/{retro_id}`

> No hace falta autenticación todavía

---

## 🧠 Tarea 5 (opcional): Identificación de participante

**Objetivo:** Identificar al participante que se une a una retro si no está definido.

**Requisitos sugeridos:**
- Si no se provee `participant_id`, mostrar input para que lo ingrese
- Alternativamente: crear un participante anónimo y asignarlo automáticamente
- Asociarlo a la retro en DB y devolver su `participant_id` embebido en la vista

---

### 🏷 Sugerencias de etiquetas para Codex

- `type:feature`
- `area:websocket` (para tareas 1 y 2)
- `area:frontend`
- `difficulty:easy` o `medium`
