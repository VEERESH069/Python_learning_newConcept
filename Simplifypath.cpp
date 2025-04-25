class Solution {
    public:
        string simplifyPath(string path) {
            vector<string>v;
            int n = path.length();
            string res ;
            for(int i=0;i<n;i++){
                string dir = "";
                while(i<n and path[i]!='/'){
                    dir+=path[i];
                    i++;
                }
              if (dir == "..") {
                if (!v.empty())
                    v.pop_back();
            }else if (dir == "." || dir == "") {
            }else{
                    v.push_back(dir);
                }
            }
            for(string i:v){
                res+="/"+i;
            }
            if(res==""){
                return "/";
            }
            return res;
        }
    };
    