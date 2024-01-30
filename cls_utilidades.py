
class Utilidades:
    def get_last_id(self,lst_items:list[dict]) -> str:
        lst_ids_str :list[str] = [item.get('id') for item in lst_items]
        lst_ids_num = [id_str.split('-')[1] for id_str in lst_ids_str]
        if lst_ids_str[0].split('-')[0] == 'l':
            prefix = 'l'
        else:
            prefix = 'm'
        ultimo_id = prefix + '-' + str(max(lst_ids_num).zfill(4))
        
        return ultimo_id
    
    def get_next_id(self,lst_items:list[dict]) -> str:
        
        if len(lst_items) == 0:
            return None
        else:
            last_id  = self.get_last_id(lst_items)
            last_id_inf = last_id.split('-')
            next_id_num = int(last_id_inf[1]) + 1
            return last_id_inf[0] +'-'+ str(next_id_num).zfill(4)
    
    def check_string_in_dict(self,search_str:str,key_name:str,lst_itens:list[dict]) -> bool:
        for item in lst_itens:
            value :str = item.get(key_name)
            if value.lower() == search_str.lower():
                return True
        return False
        