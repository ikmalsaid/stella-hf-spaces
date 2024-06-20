from modules.engine_v2 import *
feature = 'Text-to-Image - V2 / V3'
'''
_____________________________________________________________________

  Copyright © 2023-2024 Ikmal Said. All rights reserved.
   
  This program is the property of Ikmal Said. You may not reproduce
  distribute, or modify this code without the express permission of 
  the author, Ikmal Said.
_____________________________________________________________________
                                                                     
'''
with ui.Blocks(css=css, title=title(feature), theme=theme, analytics_enabled=False) as stella:
    with ui.Group():  
        result_v2 = ui.Gallery(show_label=False, object_fit="contain", height="50vh", show_share_button=False)  
        prompt_v2 = ui.Textbox(label=sprompt, placeholder=spholder)
        with ui.Row():
            clear_v2 = ui.ClearButton(value="Reset", components=[result_v2, prompt_v2])
            submit_v2= ui.Button("Submit", variant="primary")
                
        with ui.Accordion('More options'):        
            style_v2 = ui.Dropdown(label=sstyle, choices=list(stella_v2.keys()), value='None', filterable=False)
            model_v2 = ui.Dropdown(label=smodel, choices=list(ckpt_v2.keys()), value='Creative V3', filterable=False)
            ratio_v2 = ui.Dropdown(label=sratio, choices=list(ratio.keys()), value='Square (1:1)', filterable=False)
            quality_v2 = ui.Dropdown(label=squality, choices=quality, value='Enhanced', filterable=False)
            smart_v2 = ui.Dropdown(label=ssmart, choices=smart, value='Disabled', filterable=False)
            with ui.Row():
                seedtype_v2 = ui.Dropdown(label='Seed type:', choices=['Randomized', 'Fixed'], value='Randomized', filterable=False)
                seedno_v2 = ui.Number(label='Seed value:', value=0, minimum=0, maximum=max_seed, visible=False)

    process_v2 = submit_v2.click(fn=queue_v2, inputs=[prompt_v2, model_v2, style_v2, ratio_v2, quality_v2, smart_v2, seedtype_v2, seedno_v2], outputs=[result_v2, result_v2])
    prompt_v2.submit(fn=queue_v2, inputs=[prompt_v2, model_v2, style_v2, ratio_v2, quality_v2, smart_v2, seedtype_v2, seedno_v2], outputs=[result_v2, result_v2])
    seedtype_v2.select(fn=seeds, inputs=seedtype_v2, outputs=seedno_v2)

if __name__ == "__main__":
    stella.queue(default_concurrency_limit=100).launch(inbrowser=True, favicon_path="favicon.ico")