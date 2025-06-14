import gradio as gr

def radhika_ai(input_text):
    return f"तिमीले लेख्न खोजेको विषय: {input_text}"

iface = gr.Interface(fn=radhika_ai, inputs="text", outputs="text", title="Radhika Ma Vi")
iface.launch()
