__docstring__ = ""


class Review():
    # The XML root is has a <ProjNet> tag.
    # There are two children of the ProjNet (root) are:
    #   1. <DrChecks> which is basically the project info
    #   2. <Comments> which contain all the comments
    def __init__(self, xml_root) -> None:
        self.project_info = ProjectInfo(xml_root.find('./DrChecks'))
        self.comments = []
        temp = xml_root.findall('./Comments/*')
        for aComment in temp:
            self.comments.append(Comment(aComment))


class Remark():
    # Parent class that isn't directly instantiated by the user.
    def __init__(self, xml_element) -> None:
        self._node = xml_element
        self.properties = {}
        for item in self._property_list:
            self.properties[item] = self.read_from_element(item)

    def read_from_element(self, attr):
        try:
            temp = self._node.find(f'./{attr}').text
            match attr:
                case 'status' | 'critical' | 'Discipline' | 'DocType' | 'CoordinatingDiscipline':
                    return temp.lower()
                case 'attachment':
                    return True if temp != None else False
                case 'createdOn':
                    return temp
                case 'impactScope' | 'impactCost' | 'impactTime':
                    return True if temp != 'No' else False
                case 'evaluations' | 'backchecks':
                    return []
                case _:
                    return self._node.find(f'./{attr}').text.replace('<br />', '\n')
        except:
            return ""

    def print_all(self):
        for item in self.properties:
            print(f'{item}: {self.properties[item]}')

    def print_single(self, attr = 'id'):
        try:
            print(f'{attr}: {self.properties[attr]}')
        except:
            print(f'\"{attr}\" was not found in the properties list.')        

    @property
    def text(self):
        pass        # this has to be handled in the child classes
    
    @property
    def id(self):
        return self.properties['id']
    
    @property
    def status(self):
        return self.properties['status']

    @property
    def createdBy(self):
        return self.properties['createdBy']
    
    @property
    def createdOn(self):
        return self.properties['createdOn'] # TODO cast to date

    @property
    def hasAttachment(self):
        return self.properties['attachment']



class ProjectInfo(Remark):
    _property_list = ['ProjectID',
                      'ProjectControlNbr',
                      'ProjectName',
                      'ReviewID',
                      'ReviewName']

    def __init__(self, xml_element) -> None:
        super().__init__(xml_element)



class Comment(Remark):

    _property_list = ['id', 
                      'spec', 
                      'sheet', 
                      'detail', 
                      'critical',               
                      'commentText',
                      'DocRef',
                      'attachment', 
                      'createdBy',
                      'createdOn', 
                      'status',        
                      'Discipline',            
                      'DocType',                
                      'CoordinatingDiscipline',
                      'evaluations',
                      'backchecks']
    
    def __init__(self, xml_element) -> None:
        super().__init__(xml_element)
        try:
            eval_elements = xml_element.findall('./evaluations/*')
            for eval_element in eval_elements:
                eval = Evaluation(eval_element)
                self.properties['evaluations'].append(eval)
        except:
            pass
        try:
            bc_elements = xml_element.findall('./backchecks/*')
            for bc_element in bc_elements:
                backcheck = Backcheck(bc_element)
                self.properties['backchecks'].append(backcheck)
        except:
            pass

    @property
    def evaluations(self):
        return self.properties['evaluations']

    @property
    def backchecks(self):
        return self.properties['backchecks']

    @property
    def evaluations_count(self):
        return len(self.properties['evaluations'])

    @property
    def backchecks_count(self):
        return len(self.properties['backchecks'])

    @property
    def text(self):
        return self.properties['commentText']


class Evaluation(Remark):
    
    _property_list = ['id', 
                      'comment', 
                      'status', 
                      'impactScope', 
                      'impactCost',               
                      'impactTime',
                      'evaluationText',
                      'attachment', 
                      'createdBy',
                      'createdOn']
    
    def __init__(self, xml_element) -> None:
        super().__init__(xml_element)
        
    @property
    def text(self):
        return self.properties['evaluationText']


class Backcheck(Remark):

    _property_list = ['id', 
                      'comment', 
                      'evaluation', 
                      'status', 
                      'backcheckText',               
                      'attachment', 
                      'createdBy',
                      'createdOn']
    
    def __init__(self, xml_element) -> None:
        super().__init__(xml_element)
        
    @property
    def text(self):
        return self.properties['backcheckText']