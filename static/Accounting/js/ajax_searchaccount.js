/**
 * Created by Ari_ on 13/12/17.
 */
var $j = jQuery.noConflict();

$j(document).on('ready', main);

function main() {
    //$j('#searchaccount').on('click', search);
    $j('#searchaccount').trigger("click");
}

//http://127.0.0.1:8000/accounting/search_accounts?name=Cuenta%202&number=2&subsidiary_account_array=1&
// nature_account_array=2&grouping_code_array=2&level=2&item=2
function search(originButton) {
    var subsidiary_account_array = $j("#msSubsidiaryAccountArray").multiselect("getChecked").map(function () {
        return this.value;
    }).get();
    var nature_account_array = $j("#msNatureAccountArray").multiselect("getChecked").map(function () {
        return this.value;
    }).get();
    var grouping_code_array = $j("#msGroupingCodeArray").multiselect("getChecked").map(function () {
        return this.value;
    }).get();

    var account = $j("#account").val();
    var number = $j("#number").val();
    var level = $j("#level").val();
    var internal_company = $j("#internal_company").val();

    if(originButton == 'search_button'){
        var url = "/accounting/search_accounts?";
    }else{
        var url = "/accounting/export_accounts?";
    }

    if (account.toString() != "") {
        url = url + "&name=" + account.toString();
    }
    if (number.toString() != "") {
        url = url + "&number=" + number.toString();
    }
    if (subsidiary_account_array.toString() != "") {
        url = url + "&subsidiary_account_array=" + subsidiary_account_array.toString();
    }
    if (nature_account_array.toString() != "") {
        url = url + "&nature_account_array=" + nature_account_array.toString();
    }
    if (grouping_code_array.toString() != "") {
        url = url + "&grouping_code_array=" + grouping_code_array.toString();
    }
    if (level.toString() != "") {
        url = url + "&level=" + level.toString();
    }

    /*if (rubro.toString() != "") {
        url = url + "&rubro=" + rubro.toString();
    }*/
    if (internal_company.toString()!="") {
        url=url+"&internal_company="+internal_company.toString();
    }
    //alert(url);
    if(originButton == 'search_button'){
        searchengine(url);

    }else{
        return url;

    }
}


function searchengine(url) {
    // Setup CSRF tokens and all that good stuff so we don't get hacked
    $.ajaxSetup(
        {
            beforeSend: function (xhr, settings) {
                if (settings.type == "POST")
                    xhr.setRequestHeader("X-CSRFToken", $('[name="csrfmiddlewaretoken"]').val());
                if (settings.type == "GET")
                    xhr.setRequestHeader("X-CSRFToken", $('[name="csrfmiddlewaretoken"]').val());
            }
        }
    );

    // Get an Oauth2 access token and then do the ajax call, because SECURITY
    /*  $.get('/obras/register_by_token', function(ans) {
     var ajaxData = { access_token: ans.access_token};
     //alert(ans.access_token);*/
    var message = "";

    $.ajax({
        url: url,
        type: 'get',
        success: function (data) {
            //console.log(data);
            displayResults(data);

        },
        error: function (data) {

            /*alert('error!! ' + data.status);*/
            /* alert('Ocurrió un error al configurar el proyecto, favor de informar al administrador del sistema el siguiente código de error: ' + data.status);*/
            message = 'Ocurrió un error al realizar la búsqueda, favor de informar al administrador del sistema el siguiente código de error:\n' + data.status;
            $('#alertModal').find('.modal-body p').text(message);
            $('#alertModal').modal('show')

        }
    });


    /* });*/
}

function displayResults(data) {
    var sHtml = "";
    var sTable = "";

    $j('#divTable').html("<div></div>");
    sHtml = '<table class="table-filtros table table-striped table_s" cellspacing="0" width="100%" id="tablaResultados">'
        + ' <a  style="margin: 0;float: right;" href=#\n' +
        '                       onclick="exportAccounts()"\n' +
        '                       class="btn btn-raised btn-info btn-sm">\n' +
        '                        <i class="fa fa-file-excel-o"></i> Exportar Cuentas\n' +
        '                    </a>'
        + ' <colgroup>'
        + ' <col width="30%">'
        + ' <col width="30%">'
        + ' <col width="15%">'
        + ' <col width="8%">'
        + ' <col width="5%">'
        + ' <col width="5%">'
        + ' <col width="5%">'
        + ' </colgroup>';


    sTable = '<thead>'
        + '<tr>'
        + '<th>No.</th>'
        + '<th>Nombre</th>'
        //+ '<th>Nivel</th>'
        //+ '<th>Rubro</th>'
        //+ '<th>Subcuenta De</th>'
        + '<th>Naturaleza</th>'
        + '<th>Cód. Agrupador SAT</th>'
        + '<th style="width: 5%;" class="no-sorting">Ver</th>'
        + '<th style="width: 5%;" class="no-sorting">Editar</th>'
        + '<th style="width: 5%;" class="no-sorting">Eliminar</th>'
        + '</tr>'
        + '</thead>'
        + '<tbody>';

    for (var i = 0; i < data.length; i++) {
        var css = "btn btn-raised btn-default btn-xs";
        var detailButton = "<i class ='fa fa-eye color-default eliminar' > </i>";
        var deleteButton = "<i class ='fa fa-trash-o color-danger eliminar' > </i>";
        var changeButton = "<i class ='fa fa-pencil color-default eliminar' > </i>";

        sTable += '<tr>'
            + '<td class="result1 selectable" >' + data[i].number.replace(/(?!^)(?=(?:\d{3})+(?:\.|$))/gm, ' ') + '</td>'
            + '<td class="result1 selectable" >' + data[i].name + '</td>'
            //+ '<td class="result1 selectable">' + checkIfNone(data[i].level) + '</td>'
            //+ '<td class="result1 selectable">' + checkIfNone(data[i].item) + '</td>'
            //+ '<td class="result1 selectable">' + checkIfNone(data[i].subsidiary_account) + '</td>'
            + '<td class="result1 selectable" >' + data[i].nature_account_display + '</td>'
            + '<td class="result1 selectable" >' + data[i].grouping_code + '</td>'
            + '<td class="result1 selectable" ><a href="/admin/SharedCatalogs/account/' + data[i].id + '" target="_blank" class="'+css+'">'
            + detailButton + '</a></td>'
            + '<td class="result1 selectable"><a href="/admin/SharedCatalogs/account/' + data[i].id + '/change"  class="'+css+'">'
            + changeButton + '</a></td>'
            + '<td class="result1 selectable" ><a href="/admin/SharedCatalogs/account/' + data[i].id + '/delete" class="'+css+'">'
            + deleteButton + '</a></td>'
            + '</tr>'
    }

    sTable += '</tbody>'
        + '</table>';

    sHtml += sTable;

    sScript = '<script id="js" type="text/javascript"  class="init">'
        + '$("#tablaResultados").DataTable( {'
        + 'destroy: true,';

    sTable = 'columnDefs: ['
        + '       {'
        + '           className: "mdl-data-table__cell--non-numeric"'
        + '       }'
        + '   ],'

        + '   responsive: true,'
        + '   "bInfo": false,';

    sScript += sTable;
    sScript += ' "pageLength": 6,';

    sTable = '   "bLengthChange": false,'
        + '   "language": {'
        + '       "sProcessing": "Procesando...",'
        + '       "sLengthMenu": "Mostrar _MENU_ registros",'
        + '       "sZeroRecords": "No se encontraron resultados",'
        + '       "sEmptyTable": "La consulta no generó resultados a mostrar",'
        + '       "sInfo": "",'
        + '       "sInfoEmpty": "",'
        + '       "sInfoFiltered": "(filtrado de un total de _MAX_ registros)",'
        + '       "sInfoPostFix": "",'
        + '       "sSearch": "",'
        + '      "sUrl": "",'
        + '       "sInfoThousands": ",",'
        + '       "sLoadingRecords": "Cargando...",'
        + '       "oPaginate": {'
        + '           "sFirst": "Primero",'
        + '           "sLast": "Último",'
        + '          "sNext": ">",'
        + '           "sPrevious": "<"'
        + '}'
        + '},'
        + '} );'
        + '</script>';

    sScript += sTable;

    $j('#divTable').html(sHtml + sScript);

}


function checkIfNone(val) {
    console.log("Val is: " + val);
    if (val == 'undefined' || val == null || val == undefined || val == "None") {
        return '-';
    }
    return val;
}




// Function to export the accounts into an excel file.
function requestFile(url){
    location.href = url;
}

function exportAccounts(){
    url = search('export_button');
    requestFile(url);

}