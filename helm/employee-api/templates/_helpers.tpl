{{/*
Expand the chart name.
*/}}

{{- define "employee-api.name" -}}
{{- default .Chart.Name .Values.app.name | trunc 63 | trimSuffix "-" -}}
{{- end }}

{{/*
Create Full Name
*/}}

{{- define "employee-api.fullname" -}}
{{ printf "%s-%s" .Release.Name (include "employee-api.name" .) }}
{{- end }}

{{/*
Common Labels
*/}}

{{- define "employee-api.labels" -}}
app.kubernetes.io/name: {{ include "employee-api.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/version: {{ .Chart.AppVersion }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
helm.sh/chart: {{ .Chart.Name }}-{{ .Chart.Version }}
{{- end }}

{{- define "employee-api.selectorLabels" -}}
app.kubernetes.io/name: {{ include "employee-api.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}