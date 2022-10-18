from gettext import translation
import json
import pandas as pd

term_dictionary={
    'filter_color':{
        'EL' : "SUB rdf:type ex:OBJObject", 
        'QL' : "SUB rdf:type ex:OBJObject",
        'RL' : "SUB ex:hasColor ex:OBJ",
    },
    'filter_size':{
        'EL' : "SUB rdf:type ex:OBJObject", 
        'QL' : "SUB rdf:type ex:OBJObject",
        'RL' : "SUB ex:hasSize ex:OBJ",
    },
    'filter_shape':{
        'EL' : "SUB rdf:type ex:OBJObject", 
        'QL' : "SUB rdf:type ex:OBJObject",
        'RL' : "SUB ex:hasShape ex:OBJ",
    },
    'filter_material':{
        'EL' : "SUB rdf:type ex:OBJObject", 
        'QL' : "SUB rdf:type ex:OBJObject",
        'RL' : "SUB ex:hasMaterial ex:OBJ",
    },
    'relate':{
        'EL' : "SUB es:hasREL OBJ", 
        'QL' : "SUB rdf:hasREL OBJ",
        'RL' : "SUB ex:hasREL OBJ",
    }
}


def open_file(filename):
    data={}
    with open(filename) as f:
        data = json.load(f)
    return data
    
def add_to_set(set_,items):
    if(len(items)>0):
        set_ = list(set_)
        for item in items:
            if item not in set_:
                set_.append(item)
    return set(set_)

def to_dataframe(data):
    return pd.DataFrame(data)


def parse(tree,program):
    current = tree.get_root()
    while(len(program)>0):
        program = program[1:]
        if(len(program)>0):
            children = [ch.name for ch in current.children]
            entry = program[0]['function']
            if(len(program[0]['value_inputs'])>0):
                for val in program[0]['value_inputs']:
                    entry=entry+'-'+val
            if entry not in children:
                current = tree.add_node_and_return(current,entry)
            else:
                current = tree.get_children_by_name(current,entry)

def parse_no_att(tree,program,functions):
    current = tree.get_root()
    while(len(program)>0):
        program = program[1:]
        if(len(program)>0):
            children = [ch.name for ch in current.children]
            entry = program[0]['function']
            if entry not in functions:
                functions.append(entry)
            if entry not in children:
                current = tree.add_node_and_return(current,entry)
            else:
                current = tree.get_children_by_name(current,entry) 
    


def search(term, array):
    idx=0
    ret=-1
    while idx<len(array):
        if array[idx]==term:
            ret = idx
            break
        idx+=1
    return ret

def parse_fun_dict(program):

    subjects=['?x','?y','?z','?w','v','k','j']
    progs = program.copy()
    
    subqueries = []
    index = 0
    index_sub=-1
    
    while(index<len(program)):
        if(program[index]['function']=='scene'):
            subqueries.append([])
            index_sub+=1
        else:
            if(len(program[index]['inputs'])>1):
                subqueries.append([])
                index_sub+=1
            subqueries[index_sub].append(program[index]['function'])
        index+=1


    ##DA RIFARE
    print(subqueries)
    ends=[]
    subqueries=subqueries[::-1]

    subqueries=[sub[::-1] for sub in subqueries]
    i = 0
    while(True):
        if(i>= len(subqueries)):
            break
        if('relate' in subqueries[i]):
            idx = search('relate',subqueries[i])
            if(idx>0):
                ss =[subqueries[i][:idx],subqueries[i][idx],subqueries[i][idx+1:]]
                ends.append(ss)
            i+=1
        else :
            if(('union' in subqueries[i]) or ('intersect' in subqueries[i])):
                idx = search('union',subqueries[i])
                if(idx<0):
                    idx = search('intersect',subqueries[i])
                to_ins = subqueries[i].pop(idx)
                ends.append(subqueries[i])
                i=i+1
                if('relate' in subqueries[i]):
                    idx = search('relate',subqueries[i])
                    if(idx>0):
                        ss =[subqueries[i][:idx],subqueries[i][idx],subqueries[i][idx+1:]]
                        ends.append(ss)
                else:
                    ends.append(subqueries[i])
                i+=1
                ends.append(to_ins)
                if('relate' in subqueries[i]):
                    idx = search('relate',subqueries[i])
                    if(idx>0):
                        ss =[subqueries[i][:idx],subqueries[i][idx],subqueries[i][idx+1:]]
                        ends.append(ss)
                else:
                    ends.append(subqueries[i])
                i=i+1
            else: 
                ends.append(subqueries[i])
                i+=1

    to_query(ends)

   
    """ for sub in subqueries:
        for idx,el in enumerate(sub):
            if ((el=='union') or (el=='intersect') or (el=='relate')):
                ss =[sub[:idx-1],sub[idx],sub[idx+1:]]
                sub =sub[:idx-1]
                sub.append(ss[1])
                sub.append(ss[2])
                break """
    """
    sub_index = 0
    if(len(ends)>1):
        print(ends[-1][::-1])
        for sub in ends[:-1][::-1]:
            print('{'+str(sub[::-1])+'}')
    else:
        print(ends[0][::-1])
    
    """

    #print(subqueries)

    
        


    
    
        

    


    

    
    



def parse_fun(program):
    program=program[1:][::-1]
    tree = HierarchyTree(program[0]['function'])
    current = tree.get_root()
    found_union=False
    found_intersect=False
    while(len(program)>0):
        program = program[1:]
        if(len(program)>0):
            children = [ch.name for ch in current.children]
            entry = program[0]['function']
            if(len(program[0]['value_inputs'])>0):
                for val in program[0]['value_inputs']:
                    entry=entry+'-'+val
            if(entry=='unique'):
                continue
            if(entry=='union'):
                found_union=True
            if(entry=='intersect'):
                found_intersect=True
            if(entry=='scene'):
                if(found_union):
                    current=tree.find_by_name('union')
                elif(found_intersect):
                    current=tree.find_by_name('intersect')
                else:
                    current=tree.get_root()
            else:
                if entry not in children:
                    current = tree.add_node_and_return(current,entry)
                else:
                    current = tree.get_children_by_name(current,entry) 
    tree.print_tree()
   
    dict_tree = tree.sub_obj_visit()
    
    #print(dict_tree)
    #query=to_query(dict_tree)
    #print('QUERY')
    #print(query)

    #query_blocks = [str.replace('(','|').replace(')','|') for str in query.split('trans')[1:]]
    #query = ''.join(query_blocks)

    
    #print(query)



    #translate(query)


def clear_array(arr):
    idx=0
    while True:
        if(idx>len(arr)):
            break
        if arr[idx]=='':
            arr.pop(idx)
        idx+=1

def translate(query):
    global translation

    result = ''

    start=-1
    finish=-1
    block1=''
    block2=''
    incisive=''
    for idx1 in range(len(query)):
        if(query[idx1]=='{'):
            start=idx1
            idx2=idx1
            while True:
                idx2+=1
                if(query[idx2]=='}'):
                    finish=idx2
                    break
    if(finish>start>0):
        block1=query[:start]
        block2=query[finish+1:]
        incisive=query[start+1:finish]
    else:
        block1=query
        
    split1 = block1.split('|')
    split2 = block2.split('|')
    split3 = incisive.split('|')


    clear_array(split1)
    clear_array(split2)
    clear_array(split3)

    first = split1.pop(0)
    result+=translation[first]['A']['X']

  
    for idx,spl in enumerate(split1):
        if '-' in spl:
            
            spll = spl.split('-')
            result = result.replace('0000',translation[spll[0]]['A']['X'])
            result=result.replace('2222', spll[1].capitalize())
        else:
            if(idx==(len(split1)-1) and len(split3)>0):
                
                result=result.replace("0000",translation[spl]['B']['X'])
                
                comma_idx = split3.index(',')
                first_subquery = split3[:comma_idx]
                second_subquery = split3[comma_idx+1:]

                first_first_subquery = first_subquery.pop(0)
                if '-' in first_first_subquery:
                    spll = first_first_subquery.split('-')
                    result = result.replace('0000',translation[spll[0]]['A']['X'])
                    result=result.replace('2222', spll[1].capitalize())
                else:
                    result=result.replace('0000',translation[first_first_subquery]['A']['X'])
                relate = False
                for idx,spl in enumerate(first_subquery):
                    if '-' in spl:
                        spll = spl.split('-')
                        if(spll[0]=='relate'):
                            relate=True
                            result = result.replace('0000',translation[spll[0]]['A']['X'])
                            result=result.replace('2222', spll[1].capitalize())
                        else:
                            if (relate):
                                result = result.replace('0000',translation[spll[0]]['A']['Y'])
                                result=result.replace('2222', spll[1].capitalize())
                            else :
                                result = result.replace('0000',translation[spll[0]]['A']['X'])
                                result=result.replace('2222', spll[1].capitalize())
                    else : 
                        if (relate):
                            result = result.replace('0000',translation[spl]['A']['Y'])
                        else : 
                            result = result.replace('0000',translation[spl]['A']['X'])
                result = result.replace('0000','')
                relate = False
                first_second_subquery = second_subquery.pop(0)
                if '-' in first_second_subquery:
                    spll = first_second_subquery.split('-')
                    result = result.replace('1111',translation[spll[0]]['A']['X'])
                    result=result.replace('2222', spll[1].capitalize())
                else:
                    result=result.replace('1111',translation[first_second_subquery]['A']['X'])
                for idx,spl in enumerate(second_subquery):
                    if '-' in spl:
                        spll = spl.split('-')
                        if(spll[0]=='relate'):
                            relate=True
                            result = result.replace('0000',translation[spll[0]]['A']['X'])
                            result=result.replace('2222', spll[1].capitalize())
                        else:
                            if (relate):
                                result = result.replace('0000',translation[spll[0]]['A']['Y'])
                                result=result.replace('2222', spll[1].capitalize())
                            else :
                                result = result.replace('0000',translation[spll[0]]['A']['X'])
                                result=result.replace('2222', spll[1].capitalize())
                    else : 
                        if (relate):
                            result = result.replace('0000',translation[spl]['A']['Y'])
                        else : 
                            result = result.replace('0000',translation[spl]['A']['X'])

            else:
                result=result.replace('0000',translation[spl]['A']['X'])
    

    result = result.replace('0000','')
    result = result.replace('1111','')
    result = result.replace('2222','')
    result = result.replace('Large','Big')
    print(result)


def to_query(array):
    print(array)
    if(len(array)==1):
        array=array[0]
    print()

    question = array.pop(0)

    if(len(question)>1 and type(question) is list):
        print(question.pop(0))
        print('{')
        for rem in question:
            print(rem)    
    else:
        print(question)
        print('{')
    for idx,sub in enumerate(array):
        print(sub)

    print('}')
    
def fun(programs):
    ret = []
    for p in programs:
        ret.append(p['function'])
    string_ret=""
    for r in ret:
        string_ret+=r+'-'
    return string_ret


def compare(a,b):

    ret = False
    for idx,item in enumerate(b):
        if(ret):
            break
        else:
            for sub in a:
                if sub[idx]!=item:
                    ret = True
                    break
    return ret

def manage_relation(rel):
    rel_dict={
        'left':'hasOnRight',
        'right':'hasOnLeft',
        'front':'hasBehind',
        'behind':'hasOnFront'
    }
    return rel_dict[rel]

def translate_sparql(question,translation):
    global term_dictionary
    result={'EL':translation['EL'],'QL':translation['QL'],'RL':translation['RL']}
    subjects = ['?y','?z','?w','?k']
    subject_idx = 0
    placeholders=['0000','1111','2222','3333','4444','ex:REL']
    jumps=['exist','same_shape','same_size','same_color','same_material','query_material','query_shape','query_color','query_size','equal_material','equal_shape','equal_color','equal_size','count','union','equal_integer','less_than','greater_than','intersect']
    double_jumps=['query_material','query_shape','query_color','query_size']

    parsing_programs = question['program'][::-1]

    #for p in parsing_programs:
        #print(p['function'])

    for prog_idx in range(len(parsing_programs)):
        if parsing_programs[prog_idx]['function'] not in jumps:
            if parsing_programs[prog_idx-1]['function'] not in double_jumps:
                if parsing_programs[prog_idx]['function']=='unique' or parsing_programs[prog_idx]['function']=='scene':
                    subject_idx+=1
                    
                else:
                    if parsing_programs[prog_idx]['function']=='relate':
                        #value_inputs=manage_relation(''.join(parsing_programs[prog_idx]['value_inputs']))

                        #to_insert =term_dictionary[parsing_programs[prog_idx]['function']].copy()
                        
                        #to_insert['EL']=to_insert['EL'].replace('REL',value_inputs)
                        result['EL']=result['EL'].replace('REL',manage_relation(''.join(parsing_programs[prog_idx]['value_inputs'])))
                        #to_insert['EL']=to_insert['EL'].replace('SUB',subjects[subject_idx])
                        #to_insert['EL']=to_insert['EL'].replace('OBJ',subjects[subject_idx+1])
                        #to_insert['QL']=to_insert['QL'].replace('SUB',subjects[subject_idx])
                        #to_insert['QL']=to_insert['EL'].replace('REL',value_inputs)
                        result['QL']=result['QL'].replace('REL',manage_relation(''.join(parsing_programs[prog_idx]['value_inputs'])))
                        #to_insert['QL']=to_insert['QL'].replace('OBJ',subjects[subject_idx+1])
                        #to_insert['RL']=to_insert['RL'].replace('SUB',subjects[subject_idx])
                        #to_insert['RL']=to_insert['EL'].replace('REL',value_inputs)
                        result['RL']=result['RL'].replace('REL',manage_relation(''.join(parsing_programs[prog_idx]['value_inputs'])))
                        #to_insert['RL']=to_insert['RL'].replace('OBJ',subjects[subject_idx+1])
                    else:
                        value_inputs=''.join(parsing_programs[prog_idx]['value_inputs']).strip()
                        
                        to_insert =term_dictionary[parsing_programs[prog_idx]['function']].copy()
                        
                        to_insert['EL']=to_insert['EL'].replace('SUB',subjects[subject_idx])
                        to_insert['EL']=to_insert['EL'].replace('OBJ',value_inputs.capitalize())
                        to_insert['QL']=to_insert['QL'].replace('SUB',subjects[subject_idx])
                        to_insert['QL']=to_insert['QL'].replace('OBJ',value_inputs.capitalize())
                        to_insert['RL']=to_insert['RL'].replace('SUB',subjects[subject_idx])
                        to_insert['RL']=to_insert['RL'].replace('OBJ',value_inputs.capitalize())
                        
                        result['EL']=result['EL'].replace(placeholders[subject_idx], to_insert['EL']+ ". "+placeholders[subject_idx])
                        result['QL']=result['QL'].replace(placeholders[subject_idx], to_insert['QL']+ ". "+placeholders[subject_idx])
                        result['RL']=result['RL'].replace(placeholders[subject_idx], to_insert['RL']+ ". "+placeholders[subject_idx])
    for placeholder in placeholders:
        result['EL']=result['EL'].replace(placeholder,"" )
        result['QL']=result['QL'].replace(placeholder,"" )
        result['RL']=result['RL'].replace(placeholder,"" )
    
    return result


    """ for p in question['program'][::-1]:
        insert = ""
        print(subject_idx)
        print(p)
        
        if p['function'] not in jumps:
            if p['function']=='unique' or p['function']=='scene':
                subject_idx+=1
                print(subject_idx)    
            else:
                print(subject_idx)
                print(p['value_inputs'])

                value_inputs=''.join(p['value_inputs']).strip()
                to_insert = term_dictionary[p['function']]
                to_insert['EL']=to_insert['EL'].replace('SUB',subjects[subject_idx])
                to_insert['EL']=to_insert['EL'].replace('OBJ',value_inputs.capitalize())
                #to_insert['QL']=to_insert['QL'].replace('SUB',subjects[subject_idx])
                #to_insert['QL']=to_insert['QL'].replace('OBJ',insert.capitalize())
                #to_insert['RL']=to_insert['RL'].replace('SUB',subjects[subject_idx])
                #to_insert['RL']=to_insert['RL'].replace('OBJ',insert.capitalize())
                print(subjects[subject_idx])
                print(to_insert)
                ##result['EL']=result['EL'].replace(placeholders[subject_idx], to_insert['EL']+ ". "+placeholders[subject_idx])
                #result['QL']=result['QL'].replace(placeholders[subject_idx], to_insert['QL']+ ". "+placeholders[subject_idx])
                #result['RL']=result['RL'].replace(placeholders[subject_idx], to_insert['RL']+ ". "+placeholders[subject_idx])
        
    for p in placeholders:
        result['EL']=result['EL'].replace(p,"" )
        #result['QL']=result['QL'].replace(p,"" )
        #result['RL']=result['RL'].replace(p,"" )
    return result
             """


def main():
    translation = open_file('translator.json')
    answers = open_file('answers.json')
    
    data = open_file('./resources/questions/CLEVR_val_questions.json')['questions']
    report={}
    for idx,item in enumerate(data):
        a = input("Next")
        print(data[idx])
        print()
        print(translation[str(data[idx]['question_family_index'])]['EL'])
        print()
        print(translate_sparql(data[idx],translation[str(data[idx]['question_family_index'])]))
        """ try:
            res = translate_sparql(data[idx],translation[str(data[idx]['question_family_index'])])
        except Exception as e:
            if data[idx]['question_family_index'] not in report.keys():
                report[data[idx]['question_family_index']]=1
                print(data[idx])
            else:
                report[data[idx]['question_family_index']]=report[data[idx]['question_family_index']]+1
    """
    print(report)
    """
    groups = {}

    for d in data:
        if d['question_family_index'] in list(groups.keys()):
            groups[d['question_family_index']]['count']=groups[d['question_family_index']]['count']+1
            if(compare(groups[d['question_family_index']]['progs'],fun(d['program']))):
                groups[d['question_family_index']]['progs'].append(fun(d['program']))
        else :
            groups[d['question_family_index']]={'count':1, 'quest': d['question'],'progs':[fun(d['program'])]}
            
        
    print(groups)
    """     
    """ 
    idx=0
    while(True):
        i=input()
        print(data[idx]['question_family_index'])
        if(data[idx]['question_family_index']==0):
            print(data[idx]['question'])
        #parse_fun_dict(data[idx]['program'])
        idx+=1 """
    
   
    #tree = HierarchyTree('scene')
    #tree1 = HierarchyTree('scene')
    #functions = []
    #for question in data:
        #parse(tree,question['program'])
        #parse_no_att(tree1,question['program'],functions)
        #parse_fun(question['program'])
        #for p in question['program']:
            #functions.append(p['function'])
        #functions=list(set(functions))
    #tree.print_tree()
    #tree1.print_tree()
    #tree.export_to_dot('tree1.dot')
    #print(functions)
    """
    answers=[]
    inputs = []
    functisons = []
    value_inputs=[]
    for question in data:
        for prog in question['program']:
            for inp in prog['inputs']:
                inputs.append(inp)
            inputs=list(set(inputs))
            functions.append(prog['function'])
            functions=list(set(functions))
            for val in prog['value_inputs']:
                value_inputs.append(val)
            value_inputs=list(set(value_inputs))
        answers.append(question['answer'])
        answers=list(set(answers))
    



    table = {'answers':list(answers),'inputs':list(inputs),'functions':list(functions),'value_inputs':list(value_inputs)}

    table = to_dataframe(table)

    #print(table.head())

    #print(table.info())
    """

if __name__ == '__main__':
    main()