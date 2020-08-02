import pkg_resources
from xlwt import Workbook
from fpdf import FPDF


class PackageNameExporter:
    def __init__(self):
        self.packages = []

    def get_packages_list(self, extension, file_name):
        if extension == 'txt':
            with open(file_name, 'w') as f:
                for pkg in pkg_resources.working_set:
                    f.writelines('{name} {version}\n'.format(name=pkg.project_name, version=pkg.version))

        elif extension == 'xls':
            row = 0
            column = 0
            wb = Workbook()
            sheet1 = wb.add_sheet('Package list')

            for pkg in pkg_resources.working_set:
                sheet1.write(row, column, pkg.project_name)
                column += 1
                sheet1.write(row, column, pkg.version)
                row += 1
                column = 0

            wb.save(file_name)

        elif extension == 'pdf':
            pdf = FPDF(format='letter')  # pdf format
            pdf.add_page()  # create new page
            for index, pkg in enumerate(pkg_resources.working_set):
                pdf.set_font("Arial", size=12)
                pdf.cell(200, 10, txt="{name} == {version}".format(name=pkg.project_name, version=pkg.version),
                         ln=index, align="L")
            pdf.output(file_name)


package_class = PackageNameExporter()
package_class.get_packages_list('pdf', 'hello.pdf')
