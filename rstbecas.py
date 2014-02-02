# -*- coding: utf-8 -*-

import csv

header_label = [
    u'userid',
    u'A.1. Nombre',
    u'A.2. Correo electronico',
    u'A.3. Nombre asesor',
    u'A.4. Correo electrónico del asesor',
    u'A.5. Número de cuenta',
    u'A.6. Fecha de nacimiento',
    u'A.7. Sexo',
    u'A.8. País de recidencia permanente',
    u'A.9. Nacionalidad',
    u'A.10. Teléfono particular',
    u'A.11. Sede donde es becario',
    u'B.1. Beca',
    u'B.2. Tipo de beca que tiene actualmente',
    u'B.3. ¿Solicita cambio de parcial a completa o de completa a parcial?',
    u'B.4.1  Lugar asignado - Salón',
    u'B.4.2  Lugar asignado - Escritorio',
    u'B.5. Tiene beca económica?',
    u'B.6. Que institución otorga la beca económica?',
    u'B.7. Fecha de primer ingreso como becario en el IMATE',
    u'C.1.1. Nombre de la licenciatura',
u'C.1.2. Escuela', u'C.1.3. Fecha de ingreso a licenciatura',
u'C.1.4. Fecha de egreso de licenciatura', u'C.1.5. Porcentaje de avance',
u'C.1.6. Promedio licenciatura', u'C.1.7. Tesis de licenciatura',
u'C.2.1. Nombre de la maestría', u'C.2.2. Escuela', u'C.2.3. Fecha de ingreso a maestría',
u'C.2.4. Fecha de egreso de la maestría', u'C.2.5. Porcentaje de avance',
u'C.2.6. Promedio maestría', u'C.2.7. Exámenes generales aprobados',
u'C.2.8. Tesis/tesina de maestría', u'C.3.1. Nombre doctorado', u'C.3.2. Escuela',
u'C.3.3. Ingreso doctorado', u'C.3.4. Egreso doctorado',
u'C.3.5. Exámenes generales y de candidatura presentados a la fecha',
u'C.3.6. Tesis de doctorado', u'C.4. Informacion adicional', u'D.1.1. Periodo reportado',
u'D.1.2. Nivel', u'D.1.3. Materias cursadas en el periodo',
u'D.1.4. Porcentaje de créditos a la fecha', u'D.1.5. Promedio hasta la fecha',
u'D.1.6. Exámenes generales/candidatura aprobados en el periodo', u'D.1.7. Avance de tesis/tesina',
u'D.1.8. Información adicional', u'D.2.1. Periodo', u'D.2.2. Nivel', u'D.2.3. Materias por cursar',
u'D.2.4. Ex\xe1menes Generales/candidatura  por presentar',
u'D.2.5. Fecha probable de obtención del grado', u'D.2.6. Tesis', u'D.2.7.  Información adicional',
u'D.3. Documentos anexos (en un solo archivo)',
u'E. COMENTARIOS DE LA COMISIÓN (espacio para uso de la comisión de becas)',
u'F. Estado de la solicitud', u'Posting Date/Time']

sections = {
1: [(u'A. INFORMACIÓN GENERAL', '-')],
12: [(u'B. INFORMACIÓN DE LA BECA', '-')],
20: [(u'C. ESTUDIOS REALIZADOS', '-'), (u'C.1. LICENCIATURA', '~')],
27: [(u'C.2. MAESTRÍA', '~')],
35: [(u'C.3. DOCTORADO', '~')],
42: [(u'D INFORME', '-'), (u'D.1. INFORME DE ACTIVIDADES REALIZADAS', '~')],
50: [(u'D.2. PLAN DE ACTIVIDADES', '~')],
}

csvreader = csv.reader(open('applications.csv', 'r'), delimiter=',')
header = csvreader.next()

nameindex = 1
rows = [(row[nameindex].lower(), row) for row in csvreader]
rows.sort(key=lambda x: x[0])  # ordenamos por primer elemento

outfile = open('source/applications.rtf', 'w')

args = ['{', '\\rtf', '\pard', '\n']
outfile.write(''.join(args))

import rtfunicode


def checkforsubheader(outfile, index):
    header = sections.get(index, None)
    if header:
        for i, h in enumerate(header):
            if i == 1:
                outfile.write('{\pard\sa300')
            else:
                outfile.write('{\pard\sb300\sa300')
            outfile.write('{\\b %s}' % (h[0].encode('rtfunicode')))
            outfile.write('\par}\n')

for row in rows:
    # write Name
    name = row[1][nameindex].strip()
    outfile.write('{\pard\qc')
    outfile.write('{\\b %s}' % (name.decode('UTF-8').encode('rtfunicode')))
    outfile.write('\par}\n')

    # # Resume
    # resume = [
    #     (1, 'NOMBRE'),
    #     (41, 'NIVEL'),
    #     (3, 'ASESOR'),
    #     (12, 'TIPO DE BECA'),
    #     (13, '\¿SOLICITA CAMBIO?'),
    #     (15, 'BECA ECONOMICA'),
    # ]
    # for index, label in resume:
    #     value = row[1][index].strip()
    #     outfile.write('{\pard')
    #     outfile.write('{\\b %s: }' % label)
    #     outfile.write(value.decode('UTF-8').encode('rtfunicode'))
    #     outfile.write('\par}\n')
    # # ingreso
    # nivel = row[1][41].strip()
    # if nivel == 'Licenciatura':
    #     ingreso = row[1][20].strip()
    # elif nivel == 'Doctorado':
    #     ingreso = row[1][35].strip()
    # else:
    #     ingreso = row[1][27].strip()
    # outfile.write('{\pard')
    # outfile.write('{\\b INGRESO: }')
    # outfile.write(ingreso.decode('UTF-8').encode('rtfunicode'))
    # outfile.write('\par}\n')
    # #AVANCE
    # outfile.write('{\pard')
    # outfile.write('{\\b AVANCE: }')
    # # outfile.write(ingreso.decode('UTF-8').encode('rtfunicode'))
    # outfile.write('\par}\n')
    # # RECOMENDACION:
    # outfile.write('{\pard')
    # outfile.write('{\\b RECOMENDACION: }')
    # # outfile.write(ingreso.decode('UTF-8').encode('rtfunicode'))
    # outfile.write('\par}\n')


    # write fields
    for index, head in enumerate(header_label):
        if(head in [u'userid', u'F. Estado de la solicitud',
            u'E. COMENTARIOS DE LA COMISIÓN (espacio para uso de la comisión de becas)']):
            continue
        checkforsubheader(outfile, index)
        outfile.write('{\pard\n')
        args = ['\\b', ]
        outfile.write('{%s %s:} ' % (''.join(args), head.encode('rtfunicode')))
        text = row[1][index].split('\n')
        for line in text:
            if line is not " " and line is not "":
                outfile.write(line.strip().decode('UTF-8').encode('rtfunicode'))
        outfile.write('\par\n}')

    outfile.write('\page')


outfile.write('}')
outfile.close()
