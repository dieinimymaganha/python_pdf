from pylovepdf.ilovepdf import ILovePdf

ilovepdf = ILovePdf('project_public_1953989911d90de3ff22f2cdc529f382_ngP3Wf9ec090681fa880ac704d3b6cf1b27df', verify_ssl=True)
task = ilovepdf.new_task('compress')
task.add_file('C:\\repositorio\\teste_pdf\\document-0384212176-20200525.pdf')
task.set_output_folder('C:\\repositorio\\teste_pdf\\')
task.execute()
task.download()
task.delete_current_task()