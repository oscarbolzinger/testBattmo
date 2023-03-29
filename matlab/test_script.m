function data = test_script()
    a = "[1, 2, 3]";
    b = "2";
    d = "test";
    e = "{'test_key': 12}";
    f = "3.14";
    % values = cellstr([a; b; d; e; f]);
    
    fid = fopen(fullfile('C:\Users\oscarb\', "Documents\code\testBattmo\python\battmo_input.json"), 'r');
    raw = fread(fid,inf);
    str = char(raw');
    fclose(fid);
    data = jsondecode(str); 

    fid = fopen('battmo_output.json','w');
    fprintf(fid,'%s',jsonencode(data, "PrettyPrint", true));
    fclose(fid);
    
end
