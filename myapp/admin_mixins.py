import csv
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.utils import simpleSplit
from django.contrib.staticfiles import finders


font_path = finders.find('fonts/DejaVuSans.ttf')
if font_path:
    pdfmetrics.registerFont(TTFont('DejaVuSans', font_path))
else:
    raise FileNotFoundError("Шрифт DejaVuSans.ttf не найден в папке static/fonts")

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={meta}.csv'
        response.write('\ufeff'.encode('utf8')) 
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Экспорт в CSV"

class ExportPdfMixin:
    def export_as_pdf(self, request, queryset):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename={self.model._meta}.pdf'
        p = canvas.Canvas(response, pagesize=landscape(letter))
        p.setFont('DejaVuSans', 12)
        y = 550
        p.drawString(10, y, self.model._meta.verbose_name_plural.capitalize())
        y -= 20

        for obj in queryset:
            text = ", ".join([f"{field.verbose_name}: {getattr(obj, field.name)}" for field in self.model._meta.fields])
            y = self.draw_wrapped_text(p, text, 10, y, 750)
            y -= 10

        p.showPage()
        p.save()
        return response

    def draw_wrapped_text(self, canvas, text, x, y, max_width):
        lines = simpleSplit(text, 'DejaVuSans', 12, max_width)
        for line in lines:
            canvas.drawString(x, y, line)
            y -= 14  # Высота строки
        return y

    export_as_pdf.short_description = "Экспорт в PDF"