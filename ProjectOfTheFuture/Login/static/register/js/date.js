function day(){
    document.write('<option value="0">день</option>');
    var i = 1;
    while(i <= 31){
        var i1 = i++;
        document.write('<option value="' + i1 + '">' + i1 + '</option>');
    }
}
function month(){
    document.write('<option value="0">месяц</option>');
    var month_name = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь'];
    var g = 0;
    while(g < month_name.length){
        var g1 = g++;
        document.write('<option value="' + g1 + '">' + month_name[g1] + '</option>');
    }
}
function year(){
    document.write('<option value="0">год</option>');
    var i = 1900;
    while(i <= 2018){
        var i1 = i++;
        document.write('<option value="' + i1 + '">' + i1 + '</option>');
    }
}