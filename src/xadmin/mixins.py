

from django.utils.translation import override, gettext_lazy as _, activate, get_language_bidi
from django.contrib.admin.utils import label_for_field

class ModelMixinEssential(object):
    pass


class ModelMixinExtend(object):
    pass


class ModelMixinExport(object):
    data_len = 0
    progress_recorder = None
    allow_format = ('csv', 'txt', 'xls', 'pdf')
    operator = None

    def export_executor(self, request, progress_recorder):
        if request.LANGUAGE_CODE:
            activate(request.LANGUAGE_CODE)
        assert progress_recorder, 'progress_recorder can not be None'
        self.progress_recorder = progress_recorder
        file_format = request.GET.get('export_type', '')
        self.request_params = request.GET
        self.operator = request.user
        datas = self.get_export_data(request)
        export_headers = request.GET.get('export_headers', '').strip()
        fields = list(filter(None, export_headers.split(',')))
        if get_language_bidi():
            fields.reverse()
        headers = []
        for (index, field) in enumerate(fields):
            headers.append(str(label_for_field(field, self.model, self)))
            fields[index] = field
        file_path = self.export2file(file_format, fields, headers, datas, as_file=True)
        assert file_path, 'Export error, file_path is None'
        self.progress_recorder.set_progress(self.data_len, self.data_len, _('exportProgress.status.finished'))
        file_url = '/files{path}'.format(path=file_path.split('files')[1])
        return file_url

class ModelMixinAction(object):
    pass