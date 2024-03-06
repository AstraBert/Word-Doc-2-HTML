import mammoth
import os

def process_document(docx_doc):
    try:
        with open(docx_doc, "rb") as docx_file:
            result = mammoth.convert_to_html(docx_file)
            html = str(result.value)
            messages = str(result.messages)
        docx_file.close()
        html_tw = os.path.join(os.path.dirname(docx_doc), os.path.basename(docx_doc).split(".")[0]+".html")
        with open(html_tw, "w+") as htmlw:
            content = html.replace(u"\xa0", u" ")
            htmlw.write(content.encode("ascii","xmlcharrefreplace").decode("ascii"))
        htmlw.close()
        return f"Success! HTML file was created at {html_tw}\n\nThe following exceptions may have been raised during conversion process, but they did not affect the overall result:\n{messages}"
    except Exception as e:
        return f"An unexpected error occurred while converting docx to html. Please refer to the following link for troubleshooting: https://github.com/AstraBert/Word-Doc-2-HTML"