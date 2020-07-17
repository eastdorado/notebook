#include "CMJ.h" 
//���� 
CMJ::CMJ() 
{ 
 m_9LBD = false; 
 m_13Y = false; 
 m_4AK = false; 
 m_AKNum = 0; 
 m_MKNum = 0; 
} 
  
//���� 
CMJ::~CMJ() 
{ 
  
} 
//��ʼ�� 
void CMJ::Init() 
{ 
 m_9LBD = false; 
 m_13Y = false; 
 m_4AK = false; 
 m_AKNum = 0; 
 m_MKNum = 0; 
} 
//��������,������ 
bool CMJ::AddPai(int p_Type,int p_Value) 
{ 
 int iSize = m_MyPAIVec[p_Type].size(); 
 bool t_Find = false; 
 vector< int >::iterator Iter; 
 for(Iter = m_MyPAIVec[p_Type].begin();Iter !=m_MyPAIVec[p_Type].end(); Iter++) 
 { 
  if((*Iter)>p_Value) 
  { 
   m_MyPAIVec[p_Type].insert(Iter,p_Value); 
   t_Find = true; 
   break; 
  } 
    
 } 
   
 if(t_Find==false) 
 { 
  m_MyPAIVec[p_Type].push_back(p_Value); 
 } 
 m_LastPAI.m_Type = p_Type; 
 m_LastPAI.m_Value = p_Value; 
  
 return true; 
} 
  
//ȡ�ö�Ӧ��������ǽ������ 
int CMJ::GetPaiIndex(int p_Type,int p_Value) 
{ 
 int count = 0; 
 for(UINT i = 0 ; i < 6 ; i++ ) 
 { 
  vector< int >::iterator Iter; 
  for(Iter = m_MyPAIVec[i].begin();Iter !=m_MyPAIVec[i].end(); Iter++) 
  { 
   if(p_Type==i&&(*Iter)==p_Value) 
   { 
    return count; 
   } 
   count++; 
  } 
 } 
 return -1; 
} 
//���� 
bool CMJ::DelPai(int PaiIndex) 
{ 
 int count = 0; 
 for(UINT i = 0 ; i < 6 ; i++ ) 
 { 
  vector< int >::iterator Iter; 
  for(Iter = m_MyPAIVec[i].begin();Iter !=m_MyPAIVec[i].end(); Iter++) 
  { 
   if(count==PaiIndex) 
   { 
    m_MyPAIVec[i].erase(Iter); 
    return true; 
   } 
   count++; 
  } 
 } 
 return false; 
} 
//ɾ���� 
bool CMJ::DelPai(int p_Type,int p_Value) 
{ 
 vector< int >::iterator Iter; 
 for(Iter = m_MyPAIVec[p_Type].begin();Iter !=m_MyPAIVec[p_Type].end(); Iter++) 
 { 
  if((*Iter)==p_Value) 
  { 
   m_MyPAIVec[p_Type].erase(Iter); 
   return true; 
  } 
 } 
 return false; 
} 
//����� 
void CMJ::CleanUp() 
{ 
 for(UINT i = 0 ; i < 6 ; i++ ) 
 { 
  m_MyPAIVec[i].clear(); 
  m_ChiPAIVec[i].clear(); 
  m_PengPAIVec[i].clear(); 
  m_GangPAIVec[i].clear(); 
 } 
} 
//ȡ�ú�����Ϣ 
stGoodInfo  *CMJ::GetInfo() 
{ 
 return &m_GoodInfo; 
} 
  
//�����е��ƽ��к������� 
void CMJ::PrintAllPai() 
{ 
 cout<<" "; 
 for(UINT i = 0 ; i < 13 ; i++ ) 
 { 
  cout<<i<<" - "; 
 } 
 cout<<endl; 
 int icount = 0; 
 //���� 
 if(m_MyPAIVec[0].empty()==false) 
 { 
  vector< int >::iterator Iter; 
  for(Iter = m_MyPAIVec[0].begin();Iter !=m_MyPAIVec[0].end(); Iter++) 
  { 
   switch(*Iter) 
   { 
   case 1: 
    cout<<"[ ��]"; 
    break; 
   case 2: 
    cout<<"[ ��]"; 
    break; 
   case 3: 
    cout<<"[ ��]"; 
    break; 
  
   } 
   icount++; 
  } 
  
 } 
 cout<<endl; 
 for(UINT i =0 ; i < icount; i++ ) 
 { 
  cout<<"  "; 
 } 
 //���� 
 if(m_MyPAIVec[1].empty()==false) 
 { 
  vector< int >::iterator Iter; 
  for(Iter = m_MyPAIVec[1].begin();Iter !=m_MyPAIVec[1].end(); Iter++) 
  { 
   switch(*Iter) 
   { 
   case 1: 
    cout<<"[ ��]"; 
    break; 
   case 2: 
    cout<<"[ ��]"; 
    break; 
   case 3: 
    cout<<"[ ��]"; 
    break; 
   case 4: 
    cout<<"[ ��]"; 
    break; 
   } 
   icount++; 
  } 
 } 
 cout<<endl; 
 for(UINT i =0 ; i < icount; i++ ) 
 { 
  cout<<"  "; 
 } 
 //�� 
 if(m_MyPAIVec[2].empty()==false) 
 { 
  vector< int >::iterator Iter; 
  for(Iter = m_MyPAIVec[2].begin();Iter !=m_MyPAIVec[2].end(); Iter++) 
  { 
   cout<<"["<<(*Iter)<<"��]"; 
   icount++; 
  } 
 } 
 cout<<endl; 
 for(UINT i =0 ; i < icount; i++ ) 
 { 
  cout<<"  "; 
 } 
 //�� 
 if(m_MyPAIVec[3].empty()==false) 
 { 
  vector< int >::iterator Iter; 
  for(Iter = m_MyPAIVec[3].begin();Iter !=m_MyPAIVec[3].end(); Iter++) 
  { 
   cout<<"["<<(*Iter)<<"��]"; 
   icount++; 
  } 
 } 
 cout<<endl; 
 for(UINT i =0 ; i < icount; i++ ) 
 { 
  cout<<"  "; 
 } 
 //�� 
 if(m_MyPAIVec[4].empty()==false) 
 { 
  vector< int >::iterator Iter; 
  for(Iter = m_MyPAIVec[4].begin();Iter !=m_MyPAIVec[4].end(); Iter++) 
  { 
   cout<<"["<<(*Iter)<<"��]"; 
   icount++; 
  } 
 } 
 cout<<endl; 
 for(UINT i =0 ; i < icount; i++ ) 
 { 
  cout<<"  "; 
 } 
} 
//��һ���ƽ������ 
void CMJ::PrintPai(int p_Type,int p_Value) 
{ 
//���� 
 if(p_Type==0) 
 { 
  switch(p_Value) 
  { 
  case 1: 
   cout<<"[��]"; 
   break; 
  case 2: 
   cout<<"[��]"; 
   break; 
  case 3: 
   cout<<"[��]"; 
   break; 
  } 
 } 
 //���� 
 if(p_Type==1) 
 { 
  switch(p_Value) 
  { 
  case 1: 
   cout<<"[��]"; 
   break; 
  case 2: 
   cout<<"[��]"; 
   break; 
  case 3: 
   cout<<"[��]"; 
   break; 
  case 4: 
   cout<<"[��]"; 
   break; 
  } 
 } 
 //�� 
 if(p_Type==2) 
 { 
  cout<<"["<<p_Value<<"��]"; 
 } 
 //�� 
 if(p_Type==3) 
 { 
  cout<<"["<<p_Value<<"��]"; 
 } 
 //�� 
 if(p_Type==4) 
 { 
  cout<<"["<<p_Value<<"��]"; 
 } 
} 
  
//���� 
bool CMJ::CheckChiPai(int p_Type,int p_Value) 
{ 
 m_TempChiPAIVec.clear(); 
 //�� 
 if(m_MyPAIVec[p_Type].empty()==false) 
 { 
  int iSize = m_MyPAIVec[p_Type].size(); 
  if( iSize >= 2) 
  { 
   for(UINT i = 0 ; i < iSize-1 ; i++ ) 
   { 
    if((m_MyPAIVec[p_Type][i]==(p_Value-2))&&(m_MyPAIVec[p_Type][i+1]==(p_Value-1))) 
    { 
     stCHI t_Chi; 
     t_Chi.m_Type = p_Type; 
     t_Chi.m_Value1 = p_Value-2; 
     t_Chi.m_Value2 = p_Value-1; 
     t_Chi.m_Value3 = p_Value; 
     m_TempChiPAIVec.push_back(t_Chi); 
  
    } 
    if((m_MyPAIVec[p_Type][i]==(p_Value-1))&&(m_MyPAIVec[p_Type][i+1]==(p_Value+1))) 
    { 
     stCHI t_Chi; 
     t_Chi.m_Type = p_Type; 
     t_Chi.m_Value1 = p_Value-1; 
     t_Chi.m_Value2 = p_Value; 
     t_Chi.m_Value3 = p_Value+1; 
     m_TempChiPAIVec.push_back(t_Chi); 
  
    } 
    if((m_MyPAIVec[p_Type][i]==(p_Value+1))&&(m_MyPAIVec[p_Type][i+1]==(p_Value+2))) 
    { 
     stCHI t_Chi; 
     t_Chi.m_Type = p_Type; 
     t_Chi.m_Value1 = p_Value; 
     t_Chi.m_Value2 = p_Value+1; 
     t_Chi.m_Value3 = p_Value+2; 
     m_TempChiPAIVec.push_back(t_Chi); 
    } 
   } 
  
  } 
  //�����B������ABC 
  if( iSize >= 3) 
  { 
   for(UINT i = 1 ; i < iSize-1 ; i++ ) 
   { 
    if((m_MyPAIVec[p_Type][i-1]==(p_Value-1))&&(m_MyPAIVec[p_Type][i]==p_Value)&&(m_MyPAIVec[p_Type][i+1]==(p_Value+1))) 
    { 
     stCHI t_Chi; 
     t_Chi.m_Type = p_Type; 
     t_Chi.m_Value1 = p_Value-1; 
     t_Chi.m_Value2 = p_Value; 
     t_Chi.m_Value3 = p_Value+1; 
     m_TempChiPAIVec.push_back(t_Chi); 
    } 
   } 
  } 
  //�����B������ABBC 
  if( iSize >= 4) 
  { 
   for(UINT i = 1 ; i < iSize-2 ; i++ ) 
   { 
    if((m_MyPAIVec[p_Type][i-1]==(p_Value-1))&&(m_MyPAIVec[p_Type][i]==p_Value)&&(m_MyPAIVec[p_Type][i+2]==(p_Value+1))) 
    { 
     stCHI t_Chi; 
     t_Chi.m_Type = p_Type; 
     t_Chi.m_Value1 = p_Value-1; 
     t_Chi.m_Value2 = p_Value; 
     t_Chi.m_Value3 = p_Value+1; 
     m_TempChiPAIVec.push_back(t_Chi); 
    } 
   } 
  } 
  //�����B������ABBBC 
  if( iSize >= 5) 
  { 
   for(UINT i = 1 ; i < iSize-3 ; i++ ) 
   { 
    if((m_MyPAIVec[p_Type][i-1]==(p_Value-1))&&(m_MyPAIVec[p_Type][i]==p_Value)&&(m_MyPAIVec[p_Type][i+3]==(p_Value+1))) 
    { 
     stCHI t_Chi; 
     t_Chi.m_Type = p_Type; 
     t_Chi.m_Value1 = p_Value-1; 
     t_Chi.m_Value2 = p_Value; 
     t_Chi.m_Value3 = p_Value+1; 
     m_TempChiPAIVec.push_back(t_Chi); 
    } 
   } 
  } 
  //�����B������ABBBBC 
  if( iSize >= 6) 
  { 
   for(UINT i = 1 ; i < iSize-4 ; i++ ) 
   { 
    if((m_MyPAIVec[p_Type][i-1]==(p_Value-1))&&(m_MyPAIVec[p_Type][i]==p_Value)&&(m_MyPAIVec[p_Type][i+4]==(p_Value+1))) 
    { 
     stCHI t_Chi; 
     t_Chi.m_Type = p_Type; 
     t_Chi.m_Value1 = p_Value-1; 
     t_Chi.m_Value2 = p_Value; 
     t_Chi.m_Value3 = p_Value+1; 
     m_TempChiPAIVec.push_back(t_Chi); 
    } 
   } 
  } 
  if(m_TempChiPAIVec.size() > 0) 
  { 
   return true; 
  } 
 } 
 return false; 
} 
//���� 
bool CMJ::DoChiPai(int p_iIndex,int p_Type,int p_Value) 
{ 
 AddPai(p_Type,p_Value); 
 vector<stCHI>::iterator Iter; 
 int icount = 0; 
 for(Iter = m_TempChiPAIVec.begin(); Iter != m_TempChiPAIVec.end(); Iter++ ) 
 { 
  if(icount == p_iIndex) 
  { 
   DelPai((*Iter).m_Type,(*Iter).m_Value1); 
   DelPai((*Iter).m_Type,(*Iter).m_Value2); 
   DelPai((*Iter).m_Type,(*Iter).m_Value3); 
  
   m_ChiPAIVec[(*Iter).m_Type].push_back((*Iter).m_Value1); 
   m_ChiPAIVec[(*Iter).m_Type].push_back((*Iter).m_Value2); 
   m_ChiPAIVec[(*Iter).m_Type].push_back((*Iter).m_Value3); 
  
   return true; 
  } 
  icount++; 
 } 
 return false; 
} 
//�ԿɳԵ���Ͻ������ 
void CMJ::PrintChiChosePai() 
{ 
 cout<<"================�������======================="<<endl; 
 vector<stCHI>::iterator Iter; 
 for(Iter = m_TempChiPAIVec.begin(); Iter != m_TempChiPAIVec.end();Iter++) 
 { 
  //�� 
  if((*Iter).m_Type==2) 
  { 
   cout<<"["<<(*Iter).m_Value1<<"��"; 
   cout<<""<<(*Iter).m_Value2<<"��"; 
   cout<<""<<(*Iter).m_Value3<<"��]"; 
  } 
  //�� 
  if((*Iter).m_Type==3) 
  { 
   cout<<"["<<(*Iter).m_Value1<<"��"; 
   cout<<""<<(*Iter).m_Value2<<"��"; 
   cout<<""<<(*Iter).m_Value3<<"��]"; 
  } 
  //�� 
  if((*Iter).m_Type==4) 
  { 
   cout<<"["<<(*Iter).m_Value1<<"��"; 
   cout<<""<<(*Iter).m_Value2<<"��"; 
   cout<<""<<(*Iter).m_Value3<<"��]"; 
  } 
 } 
 cout<<endl<<"========================================="<<endl; 
} 
//�Կ�������Ͻ������ 
void CMJ::PrintPengChosePai() 
{ 
 cout<<"=====================����=================="<<endl; 
 vector<stPAI>::iterator Iter; 
 for(Iter = m_TempPengPAIVec.begin(); Iter != m_TempPengPAIVec.end();Iter++) 
 { 
  //�� 
  if((*Iter).m_Type==2) 
  { 
   cout<<"["<<(*Iter).m_Value<<"��"; 
   cout<<""<<(*Iter).m_Value<<"��"; 
   cout<<""<<(*Iter).m_Value<<"��]"; 
  } 
  //�� 
  if((*Iter).m_Type==3) 
  { 
   cout<<"["<<(*Iter).m_Value<<"��"; 
   cout<<""<<(*Iter).m_Value<<"��"; 
   cout<<""<<(*Iter).m_Value<<"��]"; 
  } 
  //�� 
  if((*Iter).m_Type==4) 
  { 
   cout<<"["<<(*Iter).m_Value<<"��"; 
   cout<<""<<(*Iter).m_Value<<"��"; 
   cout<<""<<(*Iter).m_Value<<"��]"; 
  } 
 } 
 cout<<endl<<"========================================="<<endl; 
} 
//�Կɸܵ���Ͻ������ 
void CMJ::PrintGangChosePai() 
{ 
 cout<<"====================����==================="<<endl; 
 vector<stPAI>::iterator Iter; 
 for(Iter = m_TempGangPAIVec.begin(); Iter != m_TempGangPAIVec.end();Iter++) 
 { 
  //�� 
  if((*Iter).m_Type==2) 
  { 
   cout<<"["<<(*Iter).m_Value<<"��"; 
   cout<<""<<(*Iter).m_Value<<"��"; 
   cout<<""<<(*Iter).m_Value<<"��"; 
   cout<<""<<(*Iter).m_Value<<"��]"; 
  } 
  //�� 
  if((*Iter).m_Type==3) 
  { 
   cout<<"["<<(*Iter).m_Value<<"��"; 
   cout<<""<<(*Iter).m_Value<<"��"; 
   cout<<""<<(*Iter).m_Value<<"��"; 
   cout<<""<<(*Iter).m_Value<<"��]"; 
  } 
  //�� 
  if((*Iter).m_Type==4) 
  { 
   cout<<"["<<(*Iter).m_Value<<"��"; 
   cout<<""<<(*Iter).m_Value<<"��"; 
   cout<<""<<(*Iter).m_Value<<"��"; 
   cout<<""<<(*Iter).m_Value<<"��]"; 
  } 
 } 
 cout<<endl<<"========================================="<<endl; 
} 
//ȡ�ó�������� 
UINT CMJ::GetChiChoseNum() 
{ 
 return m_TempChiPAIVec.size(); 
} 
//���� 
bool CMJ::CheckPengPai(int p_Type,int p_Value) 
{ 
 m_TempPengPAIVec.clear(); 
 //�� 
 if(m_MyPAIVec[p_Type].empty()==false) 
 { 
  int iSize = m_MyPAIVec[p_Type].size(); 
  if( iSize >= 2) 
  { 
   for(UINT i = 0 ; i < iSize-1 ; i++ ) 
   { 
    if((m_MyPAIVec[p_Type][i]==p_Value)&&(m_MyPAIVec[p_Type][i+1]==p_Value)) 
    { 
     stPAI t_Peng; 
     t_Peng.m_Type = p_Type; 
     t_Peng.m_Value = p_Value; 
     m_TempPengPAIVec.push_back(t_Peng); 
     break; 
    } 
   } 
  } 
  if(m_TempPengPAIVec.size() > 0) 
  { 
   return true; 
  } 
 } 
 return false; 
} 
//���� 
bool CMJ::DoPengPai(int p_Type,int p_Value) 
{ 
 AddPai(p_Type,p_Value); 
 vector<stPAI>::iterator Iter; 
 for(Iter = m_TempPengPAIVec.begin(); Iter != m_TempPengPAIVec.end(); Iter++ ) 
 { 
  DelPai((*Iter).m_Type,(*Iter).m_Value); 
  DelPai((*Iter).m_Type,(*Iter).m_Value); 
  DelPai((*Iter).m_Type,(*Iter).m_Value); 
  
  m_PengPAIVec[(*Iter).m_Type].push_back((*Iter).m_Value); 
  m_PengPAIVec[(*Iter).m_Type].push_back((*Iter).m_Value); 
  m_PengPAIVec[(*Iter).m_Type].push_back((*Iter).m_Value); 
  return true; 
 } 
 return false; 
} 
//���� 
bool CMJ::CheckGangPai(int p_Type,int p_Value) 
{  
 m_TempGangPAIVec.clear(); 
 //�� 
 if(m_MyPAIVec[p_Type].empty()==false) 
 { 
  int iSize = m_MyPAIVec[p_Type].size(); 
  if( iSize >= 3) 
  { 
   for(UINT i = 0 ; i < iSize-2 ; i++ ) 
   { 
    if((m_MyPAIVec[p_Type][i]==p_Value)&&(m_MyPAIVec[p_Type][i+1]==p_Value)&&(m_MyPAIVec[p_Type][i+2]==p_Value)) 
    { 
     stPAI t_Gang; 
     t_Gang.m_Type = p_Type; 
     t_Gang.m_Value = p_Value; 
     m_TempGangPAIVec.push_back(t_Gang); 
     break; 
    } 
   } 
  } 
  if(m_TempGangPAIVec.size() > 0) 
  { 
   return true; 
  } 
 } 
 return false; 
} 
//���� 
bool CMJ::DoGangPai(int p_Type,int p_Value) 
{ 
 AddPai(p_Type,p_Value); 
 vector<stPAI>::iterator Iter; 
 for(Iter = m_TempGangPAIVec.begin(); Iter != m_TempGangPAIVec.end(); Iter++ ) 
 { 
  DelPai((*Iter).m_Type,(*Iter).m_Value); 
  DelPai((*Iter).m_Type,(*Iter).m_Value); 
  DelPai((*Iter).m_Type,(*Iter).m_Value); 
  DelPai((*Iter).m_Type,(*Iter).m_Value); 
  
  //������� 
  if(m_GangPAIVec[(*Iter).m_Type].empty()) 
  { 
   m_GangPAIVec[(*Iter).m_Type].push_back((*Iter).m_Value); 
   m_GangPAIVec[(*Iter).m_Type].push_back((*Iter).m_Value); 
   m_GangPAIVec[(*Iter).m_Type].push_back((*Iter).m_Value); 
   m_GangPAIVec[(*Iter).m_Type].push_back((*Iter).m_Value); 
  } 
  else
  { 
    vector<int>::iterator Iter2; 
    for(Iter2 = m_GangPAIVec[(*Iter).m_Type].begin(); Iter2 != m_GangPAIVec[(*Iter).m_Type].end(); Iter2++ ) 
    { 
     if((*Iter2)>(*Iter).m_Value) 
     { 
      m_GangPAIVec[(*Iter).m_Type].insert(Iter2,(*Iter).m_Value); 
      m_GangPAIVec[(*Iter).m_Type].insert(Iter2,(*Iter).m_Value); 
      m_GangPAIVec[(*Iter).m_Type].insert(Iter2,(*Iter).m_Value); 
      m_GangPAIVec[(*Iter).m_Type].insert(Iter2,(*Iter).m_Value); 
      break; 
     } 
    } 
  } 
  return true; 
 } 
 return false; 
} 
//����Ƿ���� 
bool CMJ::CheckAllPai(bool GetOrPut) 
{ 
 if(GetOrPut == MJPAI_GETPAI) 
 { 
  //������ϲ 
  if(CheckD4X_HU()) 
  { 
   strcpy(m_GoodInfo.m_GoodName,"����ϲ"); 
   m_GoodInfo.m_GoodValue = 88; 
   return true; 
  } 
  //������Ԫ 
  if(CheckD3Y_HU()) 
  { 
   strcpy(m_GoodInfo.m_GoodName,"����Ԫ"); 
   m_GoodInfo.m_GoodValue = 88; 
   return true; 
  } 
  //�����һɫ 
  if(CheckL1S_HU()) 
  { 
   strcpy(m_GoodInfo.m_GoodName,"��һɫ"); 
   m_GoodInfo.m_GoodValue = 88; 
   return true; 
  } 
  //���������� 
  if(Check9LBD_HU()) 
  { 
   strcpy(m_GoodInfo.m_GoodName,"��������"); 
   m_GoodInfo.m_GoodValue = 88; 
   return true; 
  } 
  //����ĸ� 
  if(Check4Gang_HU()) 
  { 
   strcpy(m_GoodInfo.m_GoodName,"�ĸ�"); 
   m_GoodInfo.m_GoodValue = 88; 
   return true; 
  } 
  //������߶� 
  if(CheckL7D_HU()) 
  { 
   strcpy(m_GoodInfo.m_GoodName,"���߶�"); 
   m_GoodInfo.m_GoodValue = 88; 
   return true; 
  } 
  //���ʮ���� 
  if(Chekc13Y_HU()) 
  { 
   strcpy(m_GoodInfo.m_GoodName,"ʮ����"); 
   m_GoodInfo.m_GoodValue = 88; 
   return true; 
  } 
  //������۾� 
  if(CheckQY9_HU()) 
  { 
   strcpy(m_GoodInfo.m_GoodName,"���۾�"); 
   m_GoodInfo.m_GoodValue = 64; 
   return true; 
  } 
  //���С��ϲ 
  if(CheckX4X_HU()) 
  { 
   strcpy(m_GoodInfo.m_GoodName,"С��ϲ"); 
   m_GoodInfo.m_GoodValue = 64; 
   return true; 
  } 
  //���С��Ԫ 
  if(CheckX3Y_HU()) 
  { 
   strcpy(m_GoodInfo.m_GoodName,"С��Ԫ"); 
   m_GoodInfo.m_GoodValue = 64; 
   return true; 
  } 
  //����Ƿ��İ��� 
  if(Check4AK_HU()) 
  { 
   strcpy(m_GoodInfo.m_GoodName,"�İ���"); 
   m_GoodInfo.m_GoodValue = 64; 
   return true; 
  } 
  //����Ƿ�һɫ˫���� 
  if(Check1S2LH_HU()) 
  { 
   strcpy(m_GoodInfo.m_GoodName,"һɫ˫����"); 
   m_GoodInfo.m_GoodValue = 64; 
   return true; 
  } 
  //����Ƿ�һɫ��ͬ˳ 
  if(Check1S4TS_HU()) 
  { 
   strcpy(m_GoodInfo.m_GoodName,"һɫ��ͬ˳"); 
   m_GoodInfo.m_GoodValue = 48; 
   return true; 
  } 
  //����Ƿ�һɫ�Ľڸ� 
  if(Check1S4JG_HU()) 
  { 
   strcpy(m_GoodInfo.m_GoodName,"һɫ�Ľڸ�"); 
   m_GoodInfo.m_GoodValue = 48; 
   return true; 
  } 
  //����Ƿ�һɫ�Ĳ��� 
  if(Check1S4BG_HU()) 
  { 
   strcpy(m_GoodInfo.m_GoodName,"һɫ�Ĳ���"); 
   m_GoodInfo.m_GoodValue = 32; 
   return true; 
  } 
  //����Ƿ����� 
  if(Check3Gang_HU()) 
  { 
   strcpy(m_GoodInfo.m_GoodName,"����"); 
   m_GoodInfo.m_GoodValue = 32; 
   return true; 
  } 
    
  //����Ƿ��߶� 
  if(Check7D_HU()) 
  { 
   strcpy(m_GoodInfo.m_GoodName,"�߶�"); 
   m_GoodInfo.m_GoodValue = 24; 
   return true; 
  } 
  //����Ƿ����ǲ��� 
  if(Check7XBK_HU()) 
  { 
   strcpy(m_GoodInfo.m_GoodName,"���ǲ���"); 
   m_GoodInfo.m_GoodValue = 24; 
   return true; 
  } 
  //����Ƿ�ȫ˫�� 
  if(CheckQSK_HU()) 
  { 
   strcpy(m_GoodInfo.m_GoodName,"ȫ˫��"); 
   m_GoodInfo.m_GoodValue = 24; 
   return true; 
  } 
  //����Ƿ���һɫ 
  if(CheckQ1S_HU()) 
  { 
   strcpy(m_GoodInfo.m_GoodName,"��һɫ"); 
   m_GoodInfo.m_GoodValue = 24; 
   return true; 
  } 
  //����Ƿ�һɫ��ͬ˳ 
  if(Check1S3TS_HU()) 
  { 
   strcpy(m_GoodInfo.m_GoodName,"һɫ��ͬ˳"); 
   m_GoodInfo.m_GoodValue = 24; 
   return true; 
  } 
  //����Ƿ�һɫ���ڸ� 
  if(Check1S3JG_HU()) 
  { 
   strcpy(m_GoodInfo.m_GoodName,"һɫ���ڸ�"); 
   m_GoodInfo.m_GoodValue = 24; 
   return true; 
  } 
  //����Ƿ�ȫ�� 
  if(CheckQD_HU()) 
  { 
   strcpy(m_GoodInfo.m_GoodName,"ȫ��"); 
   m_GoodInfo.m_GoodValue = 24; 
   return true; 
  } 
  //����Ƿ�ȫ�� 
  if(CheckQZ_HU()) 
  { 
   strcpy(m_GoodInfo.m_GoodName,"ȫ��"); 
   m_GoodInfo.m_GoodValue = 24; 
   return true; 
  } 
  //����Ƿ�ȫС 
  if(CheckQX_HU()) 
  { 
   strcpy(m_GoodInfo.m_GoodName,"ȫС"); 
   m_GoodInfo.m_GoodValue = 24; 
   return true; 
  } 
  //����Ƿ����� 
  if(CheckQL_HU()) 
  { 
   strcpy(m_GoodInfo.m_GoodName,"����"); 
   m_GoodInfo.m_GoodValue = 16; 
   return true; 
  } 
  //����Ƿ���ɫ˫���� 
  if(Check3S2LH_HU()) 
  { 
   strcpy(m_GoodInfo.m_GoodName,"��ɫ˫����"); 
   m_GoodInfo.m_GoodValue = 16; 
   return true; 
  } 
  //����Ƿ�һɫ������ 
  if(Check1S3BG_HU()) 
  { 
   strcpy(m_GoodInfo.m_GoodName,"һɫ������"); 
   m_GoodInfo.m_GoodValue = 16; 
   return true; 
  } 
   
  //����Ƿ񵥵��� 
  if(CheckDDJ_HU()) 
  { 
   strcpy(m_GoodInfo.m_GoodName,"������"); 
   m_GoodInfo.m_GoodValue = 1; 
   return true; 
  } 
  
  //����Ƿ�ƽ�� 
  if(CheckHU()) 
  { 
   strcpy(m_GoodInfo.m_GoodName,"ƽ��"); 
   m_GoodInfo.m_GoodValue = 1; 
   return true; 
  } 
  
 }   
 else
 { 
  //�ж��Ƿ��������� 
  m_9LBD = Check9LBD_TING(); 
  if(m_9LBD)return true; 
  //�ж��Ƿ����� 
  m_13Y = Check13Y_TING(); 
  if(m_13Y)return true; 
  //�ж��Ƿ��İ��� 
  m_4AK = Check4AK_TING(); 
  if(m_4AK)return true; 
  //����Ƿ���ͷ 
  return CheckTING(); 
 } 
 return false; 
} 
  
//����Ƿ���ƣ��ţ� 
inline bool CMJ::CheckAAPai(int iValue1,int iValue2) 
{ 
 if(iValue1 == iValue2)return true; 
 return false; 
} 
  
//����Ƿ������� 
inline bool CMJ::CheckABCPai(int iValue1,int iValue2,int iValue3) 
{ 
 if(iValue1 == (iValue2-1)&&iValue2 == (iValue3-1))return true; 
 return false; 
} 
  
//����Ƿ������� 
inline bool CMJ::CheckAAAPai(int iValue1,int iValue2,int iValue3) 
{ 
 if(iValue1 == iValue2&&iValue2 == iValue3)return true; 
 return false; 
} 
  
//����Ƿ������� 
inline bool CMJ::CheckAAAAPai(int iValue1,int iValue2,int iValue3,int iValue4) 
{ 
 if(iValue1 == iValue2&&iValue2 == iValue3&&iValue3 == iValue4)return true; 
 return false; 
} 
//����Ƿ������� 
inline bool CMJ::CheckAABBCCPai(int iValue1,int iValue2,int iValue3,int iValue4,int iValue5,int iValue6) 
{ 
 if(iValue1 == iValue2&&iValue3 == iValue4&&iValue5 == iValue6) 
 { 
  if((iValue1 == iValue3-1)&&(iValue3 == iValue5-1)) 
  { 
   return true; 
  } 
 } 
 return false;  
} 
//����Ƿ�������ѹ 
inline bool CMJ::CheckAAABBBCCCPai(int iValue1,int iValue2,int iValue3,int iValue4,int iValue5,int iValue6,int iValue7,int iValue8,int iValue9) 
{ 
 if((iValue1 == iValue2&&iValue2 == iValue3)&&(iValue4 == iValue5&&iValue5 == iValue6)&&(iValue7 == iValue8&&iValue8 == iValue9)) 
 { 
  if((iValue1 == iValue4-1)&&(iValue4 == iValue7-1)) 
  { 
   return true; 
  } 
 } 
 return false; 
} 
//����Ƿ������� 
inline bool CMJ::CheckAAAABBBBCCCCPai(int iValue1,int iValue2,int iValue3,int iValue4,int iValue5,int iValue6,int iValue7,int iValue8,int iValue9,int iValue10,int iValue11,int iValue12) 
{ 
 if((iValue1 == iValue2&&iValue2 == iValue3&&iValue3 == iValue4)&&(iValue5 == iValue6&&iValue6 == iValue7&&iValue7 == iValue8)&&(iValue9 == iValue10&&iValue10 == iValue11&&iValue11 == iValue12)) 
 { 
  if((iValue1 == iValue5-1)&&(iValue5 == iValue9-1)) 
  { 
   return true; 
  } 
 } 
 return false; 
} 
//����Ƿ������� 
inline bool CMJ::CheckAABBCCDDEEFFPai(int iValue1,int iValue2,int iValue3,int iValue4,int iValue5,int iValue6,int iValue7,int iValue8,int iValue9,int iValue10,int iValue11,int iValue12) 
{ 
 if(iValue1 == iValue2&&iValue3 == iValue4&&iValue5 == iValue6&&iValue7 == iValue8&&iValue9 == iValue10&&iValue11 == iValue12) 
 { 
  if((iValue1 == iValue3-1)&&(iValue3 == iValue5-1)&&(iValue5 == iValue7-1)&&(iValue7 == iValue9-1)&&(iValue9 == iValue11-1)) 
  { 
   return true; 
  } 
 } 
 return false; 
} 
  
//����Ƿ���ƣ��ţ� 
bool CMJ::Check5Pai(int iValue1,int iValue2,int iValue3,int iValue4,int iValue5) 
{ 
 //������������Ϊ�����ұ�Ϊ�����Ż������� 
 if(CheckAAPai(iValue1,iValue2)) 
 { 
  if(Check3Pai(iValue3,iValue4,iValue5))return true; 
  
 } 
 //����м�����Ϊ�� 
 if(CheckAAAPai(iValue2,iValue3,iValue4)) 
 { 
  if(CheckABCPai(iValue1,iValue4,iValue5))return true; 
 } 
 //������������Ϊ�����ұ�Ϊ�����Ż������� 
 if(CheckAAPai(iValue4,iValue5)) 
 { 
  if(Check3Pai(iValue1,iValue2,iValue3))return true; 
 } 
  
 return false; 
} 
//����Ƿ���ƣ��ţ� 
bool CMJ::Check8Pai(int iValue1,int iValue2,int iValue3,int iValue4,int iValue5,int iValue6,int iValue7,int iValue8) 
{ 
 //������������Ϊ�����ұ�Ϊ�����Ż������� 
 if(CheckAAPai(iValue1,iValue2)) 
 { 
  return Check6Pai(iValue3,iValue4,iValue5,iValue6,iValue7,iValue8); 
 } 
  
 //������м�����Ϊ�������ұ�Ϊ�����Ż������� 
 if(CheckAAPai(iValue4,iValue5)) 
 { 
  if(Check3Pai(iValue1,iValue2,iValue3)&&Check3Pai(iValue6,iValue7,iValue8))return true; 
 } 
  
 //������ұ�����Ϊ�������Ϊ�����Ż������� 
 if(CheckAAPai(iValue7,iValue8)) 
 { 
  return Check6Pai(iValue1,iValue2,iValue3,iValue4,iValue5,iValue6); 
 } 
  
 return false; 
} 
//����Ƿ���ƣ��ţ� 
bool CMJ::Check11Pai(int iValue1,int iValue2,int iValue3,int iValue4,int iValue5,int iValue6,int iValue7,int iValue8,int iValue9,int iValue10,int iValue11) 
{ 
 //������������Ϊ�� 
 if(CheckAAPai(iValue1,iValue2)) 
 { 
  return Check9Pai(iValue3,iValue4,iValue5,iValue6,iValue7,iValue8,iValue9,iValue10,iValue11);  
 } 
  
 //������м�����Ϊ�� 
 if(CheckAAPai(iValue4,iValue5)) 
 { 
  //��AAA��ȫABC 
  if(Check3Pai(iValue1,iValue2,iValue3)&&Check6Pai(iValue4,iValue5,iValue6,iValue7,iValue8,iValue9))return true; 
 } 
  
 //������ұ�����Ϊ�� 
 if(CheckAAPai(iValue7,iValue8)) 
 { 
  //��AAA��ȫABC 
  if(Check3Pai(iValue9,iValue10,iValue11)&&Check6Pai(iValue1,iValue2,iValue3,iValue4,iValue5,iValue6))return true; 
 } 
  
 //������ұ�����Ϊ�� 
 if(CheckAAPai(iValue10,iValue11)) 
 { 
  return Check9Pai(iValue1,iValue2,iValue3,iValue4,iValue5,iValue6,iValue7,iValue8,iValue9); 
 } 
 return false; 
} 
//����Ƿ���ƣ��ţ� 
bool CMJ::Check14Pai(int iValue1,int iValue2,int iValue3,int iValue4,int iValue5,int iValue6,int iValue7,int iValue8,int iValue9,int iValue10,int iValue11,int iValue12,int iValue13,int iValue14) 
{ 
 //������������Ϊ�����ұ�Ϊ�����Ż������� 
 if(CheckAAPai(iValue1,iValue2)) 
 { 
  //��AAA��ȫABC 
  if(Check12Pai(iValue3,iValue4,iValue5,iValue6,iValue7,iValue8,iValue9,iValue10,iValue11,iValue12,iValue13,iValue14))return true; 
  return false; 
 } 
  
 //������м�����Ϊ�������ұ�Ϊ�����Ż������� 
 if(CheckAAPai(iValue4,iValue5)) 
 { 
  //��AAA��ȫABC 
  if(Check3Pai(iValue1,iValue2,iValue3)&&Check9Pai(iValue6,iValue7,iValue8,iValue9,iValue10,iValue11,iValue12,iValue13,iValue14))return true; 
  return false; 
 } 
  
 //������м�����Ϊ�������ұ�Ϊ�����Ż������� 
 if(CheckAAPai(iValue7,iValue8)) 
 { 
  //��AAA��ȫABC 
  if(Check6Pai(iValue1,iValue2,iValue3,iValue4,iValue5,iValue6)&&Check6Pai(iValue9,iValue10,iValue11,iValue12,iValue13,iValue14))return true; 
  return false; 
 } 
  
 //������м�����Ϊ�������ұ�Ϊ�����Ż������� 
 if(CheckAAPai(iValue10,iValue11)) 
 { 
  //��AAA��ȫABC 
  if(Check3Pai(iValue12,iValue13,iValue14)&&Check9Pai(iValue1,iValue2,iValue3,iValue4,iValue5,iValue6,iValue7,iValue8,iValue9))return true; 
  return false; 
 } 
  
 //������ұ�����Ϊ�������ұ�Ϊ�����Ż������� 
 if(CheckAAPai(iValue13,iValue14)) 
 { 
  //��AAA��ȫABC 
  if(Check12Pai(iValue1,iValue2,iValue3,iValue4,iValue5,iValue6,iValue7,iValue8,iValue9,iValue10,iValue11,iValue12))return true; 
 } 
 return false; 
} 
//����Ƿ���ƣ��ţ� 
bool CMJ::Check3Pai(int iValue1,int iValue2,int iValue3) 
{ 
 if(CheckABCPai(iValue1,iValue2,iValue3))return true; 
 if(CheckAAAPai(iValue1,iValue2,iValue3))return true; 
 return false; 
} 
//����Ƿ���ƣ��ţ� 
bool CMJ::Check6Pai(int iValue1,int iValue2,int iValue3,int iValue4,int iValue5,int iValue6) 
{ 
 if(Check3Pai(iValue1,iValue2,iValue3)&&Check3Pai(iValue4,iValue5,iValue6))return true; 
 if(Check3Pai(iValue1,iValue2,iValue3)&&Check3Pai(iValue4,iValue5,iValue6))return true; 
 //������ 
 if(CheckAABBCCPai(iValue1,iValue2,iValue3,iValue4,iValue5,iValue6))return true; 
 //��һ���������� 
 if(CheckAAAAPai(iValue2,iValue3,iValue4,iValue5)) 
 { 
  if(CheckABCPai(iValue1,iValue2,iValue6))return true; 
 } 
 return false; 
} 
  
//����Ƿ���ƣ��ţ� 
bool CMJ::Check9Pai(int iValue1,int iValue2,int iValue3,int iValue4,int iValue5,int iValue6,int iValue7,int iValue8,int iValue9) 
{ 
 if(CheckABCPai(iValue1,iValue2,iValue3)&&Check6Pai(iValue4,iValue5,iValue6,iValue7,iValue8,iValue9))return true; 
 if(CheckAAAPai(iValue1,iValue2,iValue3)&&Check6Pai(iValue4,iValue5,iValue6,iValue7,iValue8,iValue9))return true; 
 if(CheckABCPai(iValue7,iValue8,iValue9)&&Check6Pai(iValue1,iValue2,iValue3,iValue4,iValue5,iValue6))return true; 
 if(CheckAAAPai(iValue7,iValue8,iValue9)&&Check6Pai(iValue1,iValue2,iValue3,iValue4,iValue5,iValue6))return true; 
  
 return false; 
} 
  
//����Ƿ���ƣ��ţ� 
bool CMJ::Check12Pai(int iValue1,int iValue2,int iValue3,int iValue4,int iValue5,int iValue6,int iValue7,int iValue8,int iValue9,int iValue10,int iValue11,int iValue12) 
{ 
 if(CheckABCPai(iValue1,iValue2,iValue3)&&Check9Pai(iValue4,iValue5,iValue6,iValue7,iValue8,iValue9,iValue10,iValue11,iValue12))return true; 
 if(CheckAAAPai(iValue1,iValue2,iValue3)&&Check9Pai(iValue4,iValue5,iValue6,iValue7,iValue8,iValue9,iValue10,iValue11,iValue12))return true; 
 if(CheckABCPai(iValue10,iValue11,iValue12)&&Check9Pai(iValue1,iValue2,iValue3,iValue4,iValue5,iValue6,iValue7,iValue8,iValue9))return true; 
 if(CheckAAAPai(iValue10,iValue11,iValue12)&&Check9Pai(iValue1,iValue2,iValue3,iValue4,iValue5,iValue6,iValue7,iValue8,iValue9))return true; 
 if(Check6Pai(iValue1,iValue2,iValue3,iValue4,iValue5,iValue6)&&Check6Pai(iValue7,iValue8,iValue9,iValue10,iValue11,iValue12))return true; 
  
 return false; 
} 
//����Ƿ��Ǵ���ϲ 
bool CMJ::CheckD4X_HU() 
{ 
 //�����ϱ��ĸ� 
 if(m_GangPAIVec[1].size()==16) 
 { 
  //���� 
  for(int i = 0 ; i < 6 ; i++ ) 
  { 
   if(m_MyPAIVec[i].size()==2) 
   { 
    //����ǽ� 
    if(m_MyPAIVec[i][0] == m_MyPAIVec[i][1]) 
    { 
     return true; 
    } 
   } 
  } 
 } 
 return false; 
  
} 
   
//�����Ƿ��Ǵ���Ԫ 
bool CMJ::CheckD3Y_HU() 
{ 
 //�з������� 
 if(m_GangPAIVec[0].size()==12) 
 { 
  //���� 
  for(int i = 0 ; i < 6 ; i++ ) 
  { 
   if(m_MyPAIVec[i].size()==2) 
   { 
    //����ǽ� 
    if(m_MyPAIVec[i][0] == m_MyPAIVec[i][1]) 
    { 
     return true; 
    } 
   } 
  } 
 } 
 return false; 
} 
  
//����Ƿ���һɫ 
bool CMJ::CheckL1S_HU() 
{ 
 //ֻ׼�з��ƺ��� 
 if(m_MyPAIVec[1].size()>0)return false; 
 if(m_MyPAIVec[2].size()>0)return false; 
 if(m_MyPAIVec[4].size()>0)return false; 
 if(m_MyPAIVec[5].size()>0)return false; 
 if(m_ChiPAIVec[1].size()>0)return false; 
 if(m_ChiPAIVec[2].size()>0)return false; 
 if(m_ChiPAIVec[4].size()>0)return false; 
 if(m_ChiPAIVec[5].size()>0)return false; 
 if(m_PengPAIVec[1].size()>0)return false; 
 if(m_PengPAIVec[2].size()>0)return false; 
 if(m_PengPAIVec[4].size()>0)return false; 
 if(m_PengPAIVec[5].size()>0)return false; 
 if(m_GangPAIVec[1].size()>0)return false; 
 if(m_GangPAIVec[2].size()>0)return false; 
 if(m_GangPAIVec[4].size()>0)return false; 
 if(m_GangPAIVec[5].size()>0)return false; 
 //�Է��� 
 if(m_MyPAIVec[0].size() ==2) 
 { 
  if(m_MyPAIVec[0][0]==2&&m_MyPAIVec[0][1]==2) 
  { 
   for(int i = 1 ;i < 6 ; i++) 
   { 
    if(i==3)continue; 
    if(m_MyPAIVec[i].size()>0)return false; 
    if(m_ChiPAIVec[i].size()>0)return false; 
    if(m_PengPAIVec[i].size()>0)return false; 
    if(m_GangPAIVec[i].size()>0)return false; 
   } 
   //�� 
   int iSize = m_ChiPAIVec[3].size(); 
   if(iSize>0) 
   { 
    vector< int >::iterator Iter; 
    for(Iter = m_ChiPAIVec[3].begin();Iter != m_ChiPAIVec[3].end();Iter++ ) 
    { 
     if((*Iter)==1)return false; 
     if((*Iter)==5)return false; 
     if((*Iter)==7)return false; 
     if((*Iter)==9)return false; 
    } 
   } 
   //�� 
   iSize = m_PengPAIVec[3].size(); 
   if(iSize>0) 
   { 
    vector< int >::iterator Iter; 
    for(Iter = m_PengPAIVec[3].begin();Iter != m_PengPAIVec[3].end();Iter++ ) 
    { 
     if((*Iter)==1)return false; 
     if((*Iter)==5)return false; 
     if((*Iter)==7)return false; 
     if((*Iter)==9)return false; 
    } 
   } 
   //�� 
   iSize = m_GangPAIVec[3].size(); 
   if(iSize>0) 
   { 
    vector< int >::iterator Iter; 
    for(Iter = m_GangPAIVec[3].begin();Iter != m_GangPAIVec[3].end();Iter++ ) 
    { 
     if((*Iter)==1)return false; 
     if((*Iter)==5)return false; 
     if((*Iter)==7)return false; 
     if((*Iter)==9)return false; 
    } 
   } 
   //�� 
   iSize = m_MyPAIVec[3].size(); 
   if(iSize>0) 
   { 
    vector< int >::iterator Iter; 
    for(Iter = m_MyPAIVec[3].begin();Iter != m_MyPAIVec[3].end();Iter++ ) 
    { 
     if((*Iter)==1)return false; 
     if((*Iter)==5)return false; 
     if((*Iter)==7)return false; 
     if((*Iter)==9)return false; 
    } 
  
   } 
  } 
 } 
 else
 { 
  return false; 
 } 
 //��������� 
 if(m_MyPAIVec[3].size() == 3) 
 { 
  if(Check3Pai(m_MyPAIVec[3][0],m_MyPAIVec[3][1],m_MyPAIVec[3][2]))return true; 
 } 
 //��������� 
 if(m_MyPAIVec[3].size() == 6) 
 { 
  if(Check6Pai(m_MyPAIVec[3][0],m_MyPAIVec[3][1],m_MyPAIVec[3][2],m_MyPAIVec[3][3],m_MyPAIVec[3][4],m_MyPAIVec[3][5]))return true; 
 } 
 //���� 
 if(m_MyPAIVec[3].size() == 9) 
 { 
  if(Check9Pai(m_MyPAIVec[3][0],m_MyPAIVec[3][1],m_MyPAIVec[3][2],m_MyPAIVec[3][3],m_MyPAIVec[3][4],m_MyPAIVec[3][5],m_MyPAIVec[3][6],m_MyPAIVec[3][7],m_MyPAIVec[3][8]))return true; 
 } 
 //ʮ���� 
 if(m_MyPAIVec[3].size() == 12) 
 { 
  if(Check12Pai(m_MyPAIVec[3][0],m_MyPAIVec[3][1],m_MyPAIVec[3][2],m_MyPAIVec[3][3],m_MyPAIVec[3][4],m_MyPAIVec[3][5],m_MyPAIVec[3][6],m_MyPAIVec[3][7],m_MyPAIVec[3][8],m_MyPAIVec[3][9],m_MyPAIVec[3][10],m_MyPAIVec[3][11]))return true; 
 } 
 return false; 
} 
  
//����Ƿ�������ƣ����� 
bool CMJ::Check9LBD_HU() 
{ 
 if(m_9LBD)//����Ѿ��ɾ����������� 
 { 
  if(m_MyPAIVec[2].size()==14)return true; 
  if(m_MyPAIVec[3].size()==14)return true; 
  if(m_MyPAIVec[4].size()==14)return true; 
 } 
 return false; 
} 
//����Ƿ�����������ͣ����� 
bool CMJ::Check9LBD_TING() 
{ 
 for(UINT i = 2 ; i < 5 ; i++ ) 
 { 
  if(m_MyPAIVec[i].size()==13) 
  { 
   if(m_MyPAIVec[i][0]==1&&m_MyPAIVec[i][1]==1&&m_MyPAIVec[i][2]==1) 
   { 
    if(m_MyPAIVec[i][3]==2&&m_MyPAIVec[i][4]==3&&m_MyPAIVec[i][5]==4&&m_MyPAIVec[i][6]==5&&m_MyPAIVec[i][7]==6&&m_MyPAIVec[i][8]==7&&m_MyPAIVec[i][9]==8) 
    { 
     if(m_MyPAIVec[i][10]==9&&m_MyPAIVec[i][11]==9&&m_MyPAIVec[i][12]==9) 
     { 
      return true; 
     } 
    } 
   } 
  } 
 } 
  
 return false; 
} 
//����Ƿ����ĸ� 
bool CMJ::Check4Gang_HU() 
{ 
 int iSize = 0; 
 for(UINT i = 0 ; i < 6 ; i++ ) 
 { 
  iSize = m_GangPAIVec[i].size(); 
 } 
  
 if(iSize == 16) 
 { 
  //���� 
  for(int i = 0 ; i < 6 ; i++ ) 
  { 
   //����ǽ� 
   if(CheckAAPai(m_MyPAIVec[i][0],m_MyPAIVec[i][1])) 
   { 
    return true; 
   } 
  } 
    
 } 
 return false; 
} 
  
//����Ƿ����߶� 
bool CMJ::CheckL7D_HU() 
{  
 for(UINT i = 2 ; i < 5 ; i++ ) 
 { 
  if(m_MyPAIVec[i].size()==14) 
  { 
   if(m_MyPAIVec[i][0]==1&&m_MyPAIVec[i][1]==1&&m_MyPAIVec[i][2]==2&&m_MyPAIVec[i][3]==2&&m_MyPAIVec[i][4]==3&&m_MyPAIVec[i][5]==3&&m_MyPAIVec[i][6]==4&&m_MyPAIVec[i][7]==4&&m_MyPAIVec[i][8]==5&&m_MyPAIVec[i][9]==5&&m_MyPAIVec[i][10]==6&&m_MyPAIVec[i][11]==6&&m_MyPAIVec[i][12]==7&&m_MyPAIVec[i][13]==7) 
   { 
    return true; 
   } 
   if(m_MyPAIVec[i][0]==2&&m_MyPAIVec[i][1]==2&&m_MyPAIVec[i][2]==3&&m_MyPAIVec[i][3]==3&&m_MyPAIVec[i][4]==4&&m_MyPAIVec[i][5]==4&&m_MyPAIVec[i][6]==5&&m_MyPAIVec[i][7]==5&&m_MyPAIVec[i][8]==6&&m_MyPAIVec[i][9]==6&&m_MyPAIVec[i][10]==7&&m_MyPAIVec[i][11]==7&&m_MyPAIVec[i][12]==8&&m_MyPAIVec[i][13]==8) 
   { 
    return true; 
   } 
   if(m_MyPAIVec[i][0]==3&&m_MyPAIVec[i][1]==3&&m_MyPAIVec[i][2]==4&&m_MyPAIVec[i][3]==4&&m_MyPAIVec[i][4]==5&&m_MyPAIVec[i][5]==5&&m_MyPAIVec[i][6]==6&&m_MyPAIVec[i][7]==6&&m_MyPAIVec[i][8]==7&&m_MyPAIVec[i][9]==7&&m_MyPAIVec[i][10]==8&&m_MyPAIVec[i][11]==8&&m_MyPAIVec[i][12]==9&&m_MyPAIVec[i][13]==9) 
   { 
    return true; 
   } 
  } 
 } 
  
 return false; 
} 
  
//����Ƿ��ʮ���� 
bool CMJ::Chekc13Y_HU() 
{ 
 if(m_13Y) 
 { 
  bool  i13YSize[13] ; 
  for(UINT i = 0 ; i < 13 ; i++ ) 
  { 
   i13YSize[i]=false; 
  } 
  //�з��� 
  vector<int>::iterator Iter; 
  for(Iter = m_MyPAIVec[0].begin();Iter != m_MyPAIVec[0].end(); Iter++ ) 
  { 
   if((*Iter)==1) 
   { 
    i13YSize[0]=true; 
   } 
   if((*Iter)==2) 
   { 
    i13YSize[1]=true; 
   } 
   if((*Iter)==3) 
   { 
    i13YSize[2]=true; 
   } 
  } 
  //���������� 
  for(Iter = m_MyPAIVec[1].begin();Iter != m_MyPAIVec[1].end(); Iter++ ) 
  { 
   if((*Iter)==1) 
   { 
    i13YSize[3]=true; 
   } 
   if((*Iter)==2) 
   { 
    i13YSize[4]=true; 
   } 
   if((*Iter)==3) 
   { 
    i13YSize[5]=true; 
   } 
   if((*Iter)==4) 
   { 
    i13YSize[6]=true; 
   } 
  } 
  //һ���� 
  for(Iter = m_MyPAIVec[2].begin();Iter != m_MyPAIVec[2].end(); Iter++ ) 
  { 
   if((*Iter)==1) 
   { 
    i13YSize[7]=true; 
   } 
   if((*Iter)==9) 
   { 
    i13YSize[8]=true; 
   } 
  } 
  
  //һ���� 
  for(Iter = m_MyPAIVec[3].begin();Iter != m_MyPAIVec[3].end(); Iter++ ) 
  { 
   if((*Iter)==1) 
   { 
    i13YSize[9]=true; 
   } 
   if((*Iter)==9) 
   { 
    i13YSize[10]=true; 
   } 
  } 
  
  //һ�ű� 
  for(Iter = m_MyPAIVec[4].begin();Iter != m_MyPAIVec[4].end(); Iter++ ) 
  { 
   if((*Iter)==1) 
   { 
    i13YSize[11]=true; 
   } 
   if((*Iter)==9) 
   { 
    i13YSize[12]=true; 
   } 
  } 
  int icount = 0; 
  for(UINT i = 0 ; i < 13 ; i++ ) 
  { 
   if(i13YSize[i]==true) 
   { 
    icount++; 
   } 
  } 
  if(icount == 13)return true; 
  
 } 
 return false; 
} 
//����Ƿ����۾� 
bool CMJ::CheckQY9_HU() 
{  
 int iSize = 0; 
 int iCount = 0; 
 for(UINT i = 2 ; i < 5 ; i++ ) 
 { 
  iSize = m_GangPAIVec[i].size(); 
  iCount += iSize; 
  for(UINT j = 0 ; j < iSize ; j++ ) 
  { 
   if(m_GangPAIVec[i][j]!=1||m_GangPAIVec[i][j]!=9)return false; 
  } 
 } 
  
 if(iCount == 12) 
 { 
  if(m_MyPAIVec[2].size()==2) 
  { 
   if(m_MyPAIVec[2][0]==1&&m_MyPAIVec[2][1]==1)return true; 
   if(m_MyPAIVec[2][0]==9&&m_MyPAIVec[2][1]==9)return true; 
  } 
  
  if(m_MyPAIVec[3].size()==3) 
  { 
   if(m_MyPAIVec[3][0]==1&&m_MyPAIVec[3][1]==1)return true; 
   if(m_MyPAIVec[3][0]==9&&m_MyPAIVec[3][1]==9)return true; 
  } 
  
  if(m_MyPAIVec[4].size()==4) 
  { 
   if(m_MyPAIVec[4][0]==1&&m_MyPAIVec[4][1]==1)return true; 
   if(m_MyPAIVec[4][0]==9&&m_MyPAIVec[4][1]==9)return true; 
  } 
 } 
  
 return false; 
  
} 
//����Ƿ��С��ϲ 
bool CMJ::CheckX4X_HU() 
{ 
 //�����ϱ��ĸ� 
 if(m_GangPAIVec[1].size()==12) 
 { 
  //���Ƶ�λ�� 
  int iJiangPos = -1; 
  //���� 
  for(int i = 0 ; i < 6 ; i++ ) 
  { 
   if(m_MyPAIVec[i].size()==5) 
   { 
      
    if(Check5Pai(m_MyPAIVec[i][0],m_MyPAIVec[i][1],m_MyPAIVec[i][2],m_MyPAIVec[i][3],m_MyPAIVec[i][4])) 
    { 
     return true; 
    } 
   } 
   if(m_MyPAIVec[i].size()==2) 
   { 
    //����ǽ� 
    if(CheckAAPai(m_MyPAIVec[i][0],m_MyPAIVec[i][1])) 
    { 
     iJiangPos = i; 
     break; 
    } 
   } 
  } 
  // 
  if(iJiangPos>0) 
  { 
   for(int i = 0 ; i < 6 ; i++ ) 
   { 
    if(i!=iJiangPos) 
    { 
     if((m_MyPAIVec[i].size()==3)) 
     { 
      if(Check3Pai(m_MyPAIVec[i][0],m_MyPAIVec[i][1],m_MyPAIVec[i][2]))return true; 
     } 
    } 
   } 
  } 
 } 
 return false; 
} 
//����Ƿ��С��Ԫ 
bool CMJ::CheckX3Y_HU() 
{ 
 //�����ϱ��ĸ� 
 if(m_GangPAIVec[0].size()==8) 
 {  
  if(m_MyPAIVec[0].size()==5) 
  { 
   if(Check5Pai(m_MyPAIVec[0][0],m_MyPAIVec[0][1],m_MyPAIVec[0][2],m_MyPAIVec[0][3],m_MyPAIVec[0][4])) 
   { 
    return true; 
   } 
   else
   { 
    return false; 
   } 
  } 
  else if(m_MyPAIVec[0].size()==2) 
  { 
   //����ǽ� 
   if(CheckAAPai(m_MyPAIVec[0][0],m_MyPAIVec[0][1])==false) 
   { 
    return false; 
   } 
  } 
  else
  { 
   return false; 
  } 
  return CheckHU(); 
  
 } 
 return false; 
} 
//����Ƿ����һɫ 
bool CMJ::CheckZ1S_HU() 
{  
 //ֻ׼���� 
 if(m_MyPAIVec[2].size()>0)return false; 
 if(m_MyPAIVec[3].size()>0)return false; 
 if(m_MyPAIVec[4].size()>0)return false; 
 if(m_MyPAIVec[5].size()>0)return false; 
 if(m_ChiPAIVec[2].size()>0)return false; 
 if(m_ChiPAIVec[3].size()>0)return false; 
 if(m_ChiPAIVec[4].size()>0)return false; 
 if(m_ChiPAIVec[5].size()>0)return false; 
 if(m_PengPAIVec[2].size()>0)return false; 
 if(m_PengPAIVec[3].size()>0)return false; 
 if(m_PengPAIVec[4].size()>0)return false; 
 if(m_PengPAIVec[5].size()>0)return false; 
 if(m_GangPAIVec[2].size()>0)return false; 
 if(m_GangPAIVec[3].size()>0)return false; 
 if(m_GangPAIVec[4].size()>0)return false; 
 if(m_GangPAIVec[5].size()>0)return false; 
 int iSize = m_MyPAIVec[0].size(); 
 if(iSize > 0) 
 { 
  if(iSize == 2) 
  { 
   if(m_MyPAIVec[0][0]==m_MyPAIVec[0][1]) 
   { 
    iSize = m_MyPAIVec[1].size(); 
    if(iSize == 0)return true; 
    if(iSize == 3) 
    { 
     if(CheckAAAPai(m_MyPAIVec[1][0],m_MyPAIVec[1][1],m_MyPAIVec[1][2]))return true; 
    } 
   } 
  } 
  
 } 
 return false; 
} 
//����Ƿ��İ��� 
bool CMJ::Check4AK_HU() 
{ 
 if(m_4AK) 
 { 
  //���� 
  for(int i = 0 ; i < 6 ; i++ ) 
  { 
   if(m_MyPAIVec[i].size()==2) 
   { 
    //����ǽ� 
    if(m_MyPAIVec[i][0] == m_MyPAIVec[i][1]) 
    { 
     return true; 
    } 
   } 
  } 
 } 
 return false; 
}  
//����Ƿ�һɫ˫���� 
bool CMJ::Check1S2LH_HU() 
{ 
 //�������� 
 for(UINT i = 0 ; i <= 4; i++ ) 
 { 
  int iType = i; 
  if(m_MyPAIVec[iType].size()==14) 
  { 
  
   if(m_MyPAIVec[iType][0]==1&&m_MyPAIVec[iType][1]==1) 
   { 
  
   } 
   else
   { 
    return false; 
   } 
   if(m_MyPAIVec[iType][2]==2&&m_MyPAIVec[iType][3]==2) 
   { 
  
   } 
   else
   { 
    return false; 
   } 
   if(m_MyPAIVec[iType][4]==3&&m_MyPAIVec[iType][5]==3) 
   { 
  
   } 
   else
   { 
    return false; 
   } 
   if(m_MyPAIVec[iType][6]==5&&m_MyPAIVec[iType][7]==5) 
   { 
  
   } 
   else
   { 
    return false; 
   } 
   if(m_MyPAIVec[iType][8]==7&&m_MyPAIVec[iType][9]==7) 
   { 
  
   } 
   else
   { 
    return false; 
   } 
   if(m_MyPAIVec[iType][10]==8&&m_MyPAIVec[iType][11]==8) 
   { 
  
   } 
   else
   { 
    return false; 
   } 
   if(m_MyPAIVec[iType][12]==9&&m_MyPAIVec[iType][13]==9) 
   { 
  
   } 
   else
   { 
    return false; 
   } 
  
   return true; 
  } 
 } 
 return false; 
} 
  
//����Ƿ�һɫ��ͬ˳ 
bool CMJ::Check1S4TS_HU() 
{ 
 //�������� 
 for(UINT i = 0 ; i <= 4; i++ ) 
 { 
  int iType = i; 
  //�Թ���˳ 
  int iSize1 = m_ChiPAIVec[iType].size(); 
  //ʣ����ǽ�е�˳ 
  int iSize2 = m_MyPAIVec[iType].size(); 
  //�� 
  if(iSize1 + iSize2 >= 12) 
  { 
   //�޳Ե�˳ 
   if(iSize1==0) 
   { 
    if(iSize2==12) 
    { 
     //�������ܳ�˳ 
     if(CheckAAAABBBBCCCCPai(m_MyPAIVec[iType][0],m_MyPAIVec[iType][1],m_MyPAIVec[iType][2],m_MyPAIVec[iType][3],m_MyPAIVec[iType][4],m_MyPAIVec[iType][5],m_MyPAIVec[iType][6],m_MyPAIVec[iType][7],m_MyPAIVec[iType][8],m_MyPAIVec[iType][9],m_MyPAIVec[iType][10],m_MyPAIVec[iType][11]))return CheckHU(); 
     return false; 
    } 
    if(iSize2==14) 
    { 
     //�������ܳ�˳ 
     if((m_MyPAIVec[iType][12]==(m_MyPAIVec[iType][13]))&&CheckAAAABBBBCCCCPai(m_MyPAIVec[iType][0],m_MyPAIVec[iType][1],m_MyPAIVec[iType][2],m_MyPAIVec[iType][3],m_MyPAIVec[iType][4],m_MyPAIVec[iType][5],m_MyPAIVec[iType][6],m_MyPAIVec[iType][7],m_MyPAIVec[iType][8],m_MyPAIVec[iType][9],m_MyPAIVec[iType][10],m_MyPAIVec[iType][11]))return true; 
     //�������ܳ�˳ 
     if((m_MyPAIVec[iType][0]==(m_MyPAIVec[iType][1]))&&CheckAAAABBBBCCCCPai(m_MyPAIVec[iType][2],m_MyPAIVec[iType][3],m_MyPAIVec[iType][4],m_MyPAIVec[iType][5],m_MyPAIVec[iType][6],m_MyPAIVec[iType][7],m_MyPAIVec[iType][8],m_MyPAIVec[iType][9],m_MyPAIVec[iType][10],m_MyPAIVec[iType][11],m_MyPAIVec[iType][12],m_MyPAIVec[iType][13]))return true; 
     return false; 
    } 
   } 
   //�Ե�һ��˳ 
   if(iSize1==3) 
   { 
    if(iSize2==9) 
    { 
     //������ѹ 
     if(CheckAAABBBCCCPai(m_MyPAIVec[iType][0],m_MyPAIVec[iType][1],m_MyPAIVec[iType][2],m_MyPAIVec[iType][3],m_MyPAIVec[iType][4],m_MyPAIVec[iType][5],m_MyPAIVec[iType][6],m_MyPAIVec[iType][7],m_MyPAIVec[iType][8])) 
     { 
      if(m_ChiPAIVec[iType][0]==m_MyPAIVec[iType][0]&&m_ChiPAIVec[iType][1]==m_MyPAIVec[iType][3]&&m_ChiPAIVec[iType][2]==m_MyPAIVec[iType][6]) 
      { 
       return CheckHU(); 
      } 
     } 
     return false; 
    } 
    if(iSize2==11) 
    { 
  
     //������ѹ 
     if(CheckAAABBBCCCPai(m_MyPAIVec[iType][0],m_MyPAIVec[iType][1],m_MyPAIVec[iType][2],m_MyPAIVec[iType][3],m_MyPAIVec[iType][4],m_MyPAIVec[iType][5],m_MyPAIVec[iType][6],m_MyPAIVec[iType][7],m_MyPAIVec[iType][8])) 
     { 
      if(m_MyPAIVec[iType][9]==m_MyPAIVec[iType][10]&&m_ChiPAIVec[iType][0]==m_MyPAIVec[iType][0]&&m_ChiPAIVec[iType][1]==m_MyPAIVec[iType][3]&&m_ChiPAIVec[iType][2]==m_MyPAIVec[iType][6]) 
      { 
       return true; 
      } 
     } 
     //������ѹ 
     if(CheckAAABBBCCCPai(m_MyPAIVec[iType][2],m_MyPAIVec[iType][3],m_MyPAIVec[iType][4],m_MyPAIVec[iType][5],m_MyPAIVec[iType][6],m_MyPAIVec[iType][7],m_MyPAIVec[iType][8],m_MyPAIVec[iType][9],m_MyPAIVec[iType][10])) 
     { 
      if(m_MyPAIVec[iType][0]==m_MyPAIVec[iType][1]&&m_ChiPAIVec[iType][0]==m_MyPAIVec[iType][2]&&m_ChiPAIVec[iType][1]==m_MyPAIVec[iType][5]&&m_ChiPAIVec[iType][2]==m_MyPAIVec[iType][8]) 
      { 
       return true; 
      } 
     } 
  
     return false; 
    } 
   } 
   //�Ե�����˳ 
   if(iSize1==6) 
   { 
    if(iSize2==6) 
    { 
     //������ 
     if(CheckAABBCCPai(m_MyPAIVec[iType][0],m_MyPAIVec[iType][1],m_MyPAIVec[iType][2],m_MyPAIVec[iType][3],m_MyPAIVec[iType][4],m_MyPAIVec[iType][5])) 
     { 
      if(m_ChiPAIVec[iType][0]==m_MyPAIVec[iType][0]&&m_ChiPAIVec[iType][1]==m_MyPAIVec[iType][2]&&m_ChiPAIVec[iType][2]==m_MyPAIVec[iType][4]) 
      { 
       if(m_ChiPAIVec[iType][3]==m_MyPAIVec[iType][0]&&m_ChiPAIVec[iType][4]==m_MyPAIVec[iType][2]&&m_ChiPAIVec[iType][5]==m_MyPAIVec[iType][4]) 
       { 
        return CheckHU(); 
       } 
      } 
     } 
     return false; 
    } 
    if(iSize2==8) 
    { 
     //������ 
     if(CheckAABBCCPai(m_MyPAIVec[iType][0],m_MyPAIVec[iType][1],m_MyPAIVec[iType][2],m_MyPAIVec[iType][3],m_MyPAIVec[iType][4],m_MyPAIVec[iType][5])) 
     { 
      if(m_MyPAIVec[iType][6]==m_MyPAIVec[iType][7]&&m_ChiPAIVec[iType][0]==m_MyPAIVec[iType][0]&&m_ChiPAIVec[iType][1]==m_MyPAIVec[iType][2]&&m_ChiPAIVec[iType][2]==m_MyPAIVec[iType][4]) 
      { 
       if(m_ChiPAIVec[iType][3]==m_MyPAIVec[iType][0]&&m_ChiPAIVec[iType][4]==m_MyPAIVec[iType][2]&&m_ChiPAIVec[iType][5]==m_MyPAIVec[iType][4]) 
       { 
        return true; 
       } 
  
      } 
     } 
  
     //������ 
     if(CheckAABBCCPai(m_MyPAIVec[iType][2],m_MyPAIVec[iType][3],m_MyPAIVec[iType][4],m_MyPAIVec[iType][5],m_MyPAIVec[iType][6],m_MyPAIVec[iType][7])) 
     { 
      if(m_MyPAIVec[iType][0]==m_MyPAIVec[iType][1]&&m_ChiPAIVec[iType][0]==m_MyPAIVec[iType][2]&&m_ChiPAIVec[iType][1]==m_MyPAIVec[iType][4]&&m_ChiPAIVec[iType][2]==m_MyPAIVec[iType][6]) 
      { 
       if(m_ChiPAIVec[iType][3]==m_MyPAIVec[iType][2]&&m_ChiPAIVec[iType][4]==m_MyPAIVec[iType][4]&&m_ChiPAIVec[iType][5]==m_MyPAIVec[iType][6]) 
       { 
        return true; 
       } 
      } 
     } 
  
     return false; 
    } 
   } 
   //�Ե�����˳ 
   if(iSize1==9) 
   { 
    if(iSize2==3) 
    { 
     //˳�� 
     if(CheckABCPai(m_MyPAIVec[iType][0],m_MyPAIVec[iType][1],m_MyPAIVec[iType][2])) 
     { 
      if(m_ChiPAIVec[iType][0]==m_MyPAIVec[iType][0]&&m_ChiPAIVec[iType][1]==m_MyPAIVec[iType][1]&&m_ChiPAIVec[iType][2]==m_MyPAIVec[iType][2]) 
      { 
       if(m_ChiPAIVec[iType][3]==m_MyPAIVec[iType][0]&&m_ChiPAIVec[iType][4]==m_MyPAIVec[iType][1]&&m_ChiPAIVec[iType][5]==m_MyPAIVec[iType][2]) 
       { 
        if(m_ChiPAIVec[iType][6]==m_MyPAIVec[iType][0]&&m_ChiPAIVec[iType][7]==m_MyPAIVec[iType][1]&&m_ChiPAIVec[iType][8]==m_MyPAIVec[iType][2]) 
        {     
         return CheckHU(); 
        } 
       } 
      } 
     } 
     return false; 
    } 
    if(iSize2==5) 
    { 
     //˳�� 
     if(CheckABCPai(m_MyPAIVec[iType][0],m_MyPAIVec[iType][1],m_MyPAIVec[iType][2])) 
     { 
      if(m_MyPAIVec[iType][3]==m_MyPAIVec[iType][4]&&m_ChiPAIVec[iType][0]==m_MyPAIVec[iType][0]&&m_ChiPAIVec[iType][1]==m_MyPAIVec[iType][1]&&m_ChiPAIVec[iType][2]==m_MyPAIVec[iType][2]) 
      { 
       if(m_ChiPAIVec[iType][3]==m_MyPAIVec[iType][0]&&m_ChiPAIVec[iType][4]==m_MyPAIVec[iType][1]&&m_ChiPAIVec[iType][5]==m_MyPAIVec[iType][2]) 
       { 
        if(m_ChiPAIVec[iType][6]==m_MyPAIVec[iType][0]&&m_ChiPAIVec[iType][7]==m_MyPAIVec[iType][1]&&m_ChiPAIVec[iType][8]==m_MyPAIVec[iType][2]) 
        {  
         return true; 
        } 
       } 
      } 
     } 
  
     //˳�� 
     if(CheckABCPai(m_MyPAIVec[iType][2],m_MyPAIVec[iType][3],m_MyPAIVec[iType][4])) 
     { 
      if(m_MyPAIVec[iType][0]==m_MyPAIVec[iType][1]&&m_ChiPAIVec[iType][0]==m_MyPAIVec[iType][2]&&m_ChiPAIVec[iType][1]==m_MyPAIVec[iType][3]&&m_ChiPAIVec[iType][2]==m_MyPAIVec[iType][4]) 
      { 
       if(m_ChiPAIVec[iType][3]==m_MyPAIVec[iType][2]&&m_ChiPAIVec[iType][4]==m_MyPAIVec[iType][3]&&m_ChiPAIVec[iType][5]==m_MyPAIVec[iType][4]) 
       { 
        if(m_ChiPAIVec[iType][6]==m_MyPAIVec[iType][2]&&m_ChiPAIVec[iType][7]==m_MyPAIVec[iType][3]&&m_ChiPAIVec[iType][8]==m_MyPAIVec[iType][4]) 
        {  
         return true; 
        } 
  
       } 
      } 
     } 
     return false; 
    } 
   } 
  
   //�Ե�����˳ 
   if(iSize1==12) 
   { 
    if((m_ChiPAIVec[iType][0]==m_ChiPAIVec[iType][3])&&(m_ChiPAIVec[iType][3]==m_ChiPAIVec[iType][6])&&(m_ChiPAIVec[iType][6]==m_ChiPAIVec[iType][9])) 
    { 
     return CheckHU(); 
    } 
    return false; 
   } 
  } 
  
 } 
 return false; 
} 
  
//����Ƿ�һɫ�Ľڸ� 
bool CMJ::Check1S4JG_HU() 
{ 
 //�������� 
 for(UINT i = 2 ; i <= 4 ; i++) 
 { 
  int iType = i; 
  if(m_GangPAIVec[iType].size()==16) 
  { 
   if((m_GangPAIVec[iType][0]==m_GangPAIVec[iType][4]-1)&&(m_GangPAIVec[iType][4]==m_GangPAIVec[iType][8]-1)&&(m_GangPAIVec[iType][8]==m_GangPAIVec[iType][12]-1)) 
   { 
    return CheckHU(); 
   } 
  } 
 } 
 return false; 
} 
//����Ƿ�һɫ�Ĳ��� 
bool CMJ::Check1S4BG_HU() 
{ 
 /*//�� 
 if(m_GangPAIVec[2].size()==16) 
 { 
  if((m_GangPAIVec[2][0]==m_GangPAIVec[2][4]-1)&&(m_GangPAIVec[2][4]==m_GangPAIVec[2][8]-1)&&(m_GangPAIVec[2][8]==m_GangPAIVec[2][12]-1)) 
  { 
   return CheckHU(); 
  } 
 }*/
 return false; 
} 
//����Ƿ����� 
bool CMJ::Check3Gang_HU() 
{ 
 int iSize = 0; 
 for(UINT i = 0 ; i < 6 ; i++ ) 
 { 
  iSize = m_GangPAIVec[i].size(); 
 } 
  
 if(iSize == 12) 
 { 
  //���� 
  return CheckHU(); 
    
 } 
 return false; 
} 
//����Ƿ���۾� 
bool CMJ::CheckHY9_HU() 
{ 
 return false; 
} 
//����Ƿ��߶� 
bool CMJ::Check7D_HU() 
{ 
 int iDoubleNum = 0 ; 
 for(UINT i = 0 ; i < 6 ; i++ ) 
 { 
  UINT iSize = m_MyPAIVec[i].size(); 
  if(iSize%2 ==1||iSize==0)return false;//����������϶����Ƕ� 
  for(UINT j = 0 ; j < iSize-1 ; j++) 
  { 
   if(m_MyPAIVec[i][j]==m_MyPAIVec[i][j+1]) 
   { 
    iDoubleNum++; 
    j++; 
   } 
  } 
 } 
 if(iDoubleNum==7)return true; 
 return false; 
} 
//����Ƿ����ǲ��� 
bool CMJ::Check7XBK_HU() 
{ 
 bool  bIs7XBK[14] ; 
 for(UINT i = 0 ; i < 14 ; i++ ) 
 { 
  bIs7XBK[i]=false; 
 } 
 //�з��� 
 vector<int>::iterator Iter; 
 if(m_MyPAIVec[0].size()!=3)return false; 
 for(Iter = m_MyPAIVec[0].begin();Iter != m_MyPAIVec[0].end(); Iter++ ) 
 { 
  if((*Iter)==1) 
  { 
   bIs7XBK[7]=true; 
  } 
  if((*Iter)==2) 
  { 
   bIs7XBK[8]=true; 
  } 
  if((*Iter)==3) 
  { 
   bIs7XBK[9]=true; 
  } 
 } 
 //���������� 
 if(m_MyPAIVec[1].size()!=4)return false; 
 for(Iter = m_MyPAIVec[1].begin();Iter != m_MyPAIVec[1].end(); Iter++ ) 
 { 
  if((*Iter)==1) 
  { 
   bIs7XBK[10]=true; 
  } 
  if((*Iter)==2) 
  { 
   bIs7XBK[11]=true; 
  } 
  if((*Iter)==3) 
  { 
   bIs7XBK[12]=true; 
  } 
  if((*Iter)==4) 
  { 
   bIs7XBK[13]=true; 
  } 
 } 
 //��,��,�� 
 for(UINT i = 2 ; i <= 4 ; i++) 
 { 
  if(m_MyPAIVec[i].size()==3) 
  { 
   if(m_MyPAIVec[i][0]==1&&m_MyPAIVec[i][1]==4&&m_MyPAIVec[i][2]==7) 
   { 
    bIs7XBK[0]=true; 
    bIs7XBK[3]=true; 
    bIs7XBK[6]=true; 
   } 
  } 
  else if(m_MyPAIVec[2].size()==2) 
  { 
   if(m_MyPAIVec[i][0]==2&&m_MyPAIVec[i][1]==5) 
   { 
    bIs7XBK[1]=true; 
    bIs7XBK[4]=true; 
   } 
   else if(m_MyPAIVec[i][0]==3&&m_MyPAIVec[i][1]==6) 
   { 
    bIs7XBK[2]=true; 
    bIs7XBK[5]=true; 
   } 
  } 
  else
  { 
   return false; 
  } 
 } 
 bool t_Result = true; 
 for(UINT i = 0 ; i < 14 ; i++ ) 
 { 
  if(bIs7XBK[i]==false)t_Result=false; 
 } 
 if(t_Result)return true; 
  
 for(UINT i = 2 ; i <= 4 ; i++) 
 { 
  if(m_MyPAIVec[i].size()==3) 
  { 
   if(m_MyPAIVec[i][0]==2&&m_MyPAIVec[i][1]==5&&m_MyPAIVec[i][2]==8) 
   { 
    bIs7XBK[0]=true; 
    bIs7XBK[3]=true; 
    bIs7XBK[6]=true; 
   } 
  } 
  else if(m_MyPAIVec[2].size()==2) 
  { 
   if(m_MyPAIVec[i][0]==3&&m_MyPAIVec[i][1]==6) 
   { 
    bIs7XBK[1]=true; 
    bIs7XBK[4]=true; 
   } 
   else if(m_MyPAIVec[i][0]==4&&m_MyPAIVec[i][1]==7) 
   { 
    bIs7XBK[2]=true; 
    bIs7XBK[5]=true; 
   } 
  } 
  else
  { 
   return false; 
  } 
 } 
 t_Result = true; 
 for(UINT i = 0 ; i < 14 ; i++ ) 
 { 
  if(bIs7XBK[i]==false)t_Result=false; 
 } 
 if(t_Result)return true; 
  
 for(UINT i = 2 ; i <= 4 ; i++) 
 { 
  if(m_MyPAIVec[i].size()==3) 
  { 
   if(m_MyPAIVec[i][0]==3&&m_MyPAIVec[i][1]==6&&m_MyPAIVec[i][2]==9) 
   { 
    bIs7XBK[0]=true; 
    bIs7XBK[3]=true; 
    bIs7XBK[6]=true; 
   } 
  } 
  else if(m_MyPAIVec[2].size()==2) 
  { 
   if(m_MyPAIVec[i][0]==4&&m_MyPAIVec[i][1]==7) 
   { 
    bIs7XBK[1]=true; 
    bIs7XBK[4]=true; 
   } 
   else if(m_MyPAIVec[i][0]==5&&m_MyPAIVec[i][1]==8) 
   { 
    bIs7XBK[2]=true; 
    bIs7XBK[5]=true; 
   } 
  } 
  else
  { 
   return false; 
  } 
 } 
  
 t_Result = true; 
 for(UINT i = 0 ; i < 14 ; i++ ) 
 { 
  if(bIs7XBK[i]==false)t_Result=false; 
 } 
 if(t_Result)return true; 
  
 return false; 
} 
//����Ƿ�ȫ˫�� 
bool CMJ::CheckQSK_HU() 
{ 
 //�������� 
 for(UINT i = 2 ; i <= 4 ; i++) 
 { 
  int iType = i; 
  if(m_GangPAIVec[iType].size()==16) 
  { 
   if(m_GangPAIVec[iType][0]==2&&m_GangPAIVec[iType][4]==4&&m_GangPAIVec[iType][8]==6&&m_GangPAIVec[iType][12]==8) 
   { 
    return CheckHU(); 
   } 
  } 
 } 
 return false; 
} 
//��һɫ 
bool CMJ::CheckQ1S_HU() 
{ 
  
 if(m_MyPAIVec[0].empty()==false)return false; 
 if(m_MyPAIVec[1].empty()==false)return false; 
 if(m_ChiPAIVec[0].empty()==false)return false; 
 if(m_ChiPAIVec[1].empty()==false)return false; 
 if(m_PengPAIVec[0].empty()==false)return false; 
 if(m_PengPAIVec[1].empty()==false)return false; 
 if(m_GangPAIVec[0].empty()==false)return false; 
 if(m_GangPAIVec[1].empty()==false)return false; 
 //���� 
 if(m_MyPAIVec[2].empty()==false) 
 { 
  if(m_MyPAIVec[3].empty()==false)return false; 
  if(m_MyPAIVec[4].empty()==false)return false; 
  if(m_ChiPAIVec[3].empty()==false)return false; 
  if(m_ChiPAIVec[4].empty()==false)return false; 
  if(m_PengPAIVec[3].empty()==false)return false; 
  if(m_PengPAIVec[4].empty()==false)return false; 
  if(m_GangPAIVec[3].empty()==false)return false; 
  if(m_GangPAIVec[4].empty()==false)return false; 
  return CheckHU(); 
 } 
 //���� 
 if(m_MyPAIVec[3].empty()==false) 
 { 
  if(m_MyPAIVec[2].empty()==false)return false; 
  if(m_MyPAIVec[4].empty()==false)return false; 
  if(m_ChiPAIVec[2].empty()==false)return false; 
  if(m_ChiPAIVec[4].empty()==false)return false; 
  if(m_PengPAIVec[2].empty()==false)return false; 
  if(m_PengPAIVec[4].empty()==false)return false; 
  if(m_GangPAIVec[2].empty()==false)return false; 
  if(m_GangPAIVec[4].empty()==false)return false; 
  return CheckHU(); 
 } 
 //��� 
 if(m_MyPAIVec[4].empty()==false) 
 { 
  if(m_MyPAIVec[2].empty()==false)return false; 
  if(m_MyPAIVec[3].empty()==false)return false; 
  if(m_ChiPAIVec[2].empty()==false)return false; 
  if(m_ChiPAIVec[3].empty()==false)return false; 
  if(m_PengPAIVec[2].empty()==false)return false; 
  if(m_PengPAIVec[3].empty()==false)return false; 
  if(m_GangPAIVec[2].empty()==false)return false; 
  if(m_GangPAIVec[3].empty()==false)return false; 
  return CheckHU(); 
 } 
 return false; 
} 
//����Ƿ�һɫ��ͬ˳ 
bool CMJ::Check1S3TS_HU() 
{ 
 //������ 
 for(UINT i = 2 ; i <= 4 ; i++ ) 
 { 
  int iType = i; 
  //�Թ���˳ 
  int iSize1 = m_ChiPAIVec[iType].size(); 
  //ʣ����ǽ�е�˳ 
  int iSize2 = m_MyPAIVec[iType].size(); 
  if(iSize1 + iSize2 >= 9) 
  { 
   //�޳Ե�˳ 
   if(iSize1==0) 
   { 
    if(iSize2==9) 
    { 
     //������ѹ 
     if(CheckAAABBBCCCPai(m_MyPAIVec[iType][0],m_MyPAIVec[iType][1],m_MyPAIVec[iType][2],m_MyPAIVec[iType][3],m_MyPAIVec[iType][4],m_MyPAIVec[iType][5],m_MyPAIVec[iType][6],m_MyPAIVec[iType][7],m_MyPAIVec[iType][8])) 
     { 
      return CheckHU(); 
     } 
     return false; 
    } 
    if(iSize2==11) 
    { 
     //������ѹ 
     if(CheckAAABBBCCCPai(m_MyPAIVec[iType][0],m_MyPAIVec[iType][1],m_MyPAIVec[iType][2],m_MyPAIVec[iType][3],m_MyPAIVec[iType][4],m_MyPAIVec[iType][5],m_MyPAIVec[iType][6],m_MyPAIVec[iType][7],m_MyPAIVec[iType][8])&&CheckAAPai(m_MyPAIVec[iType][9],m_MyPAIVec[iType][10])) 
     { 
      return true; 
     } 
     //������ѹ 
     if(CheckAAABBBCCCPai(m_MyPAIVec[iType][2],m_MyPAIVec[iType][3],m_MyPAIVec[iType][4],m_MyPAIVec[iType][5],m_MyPAIVec[iType][6],m_MyPAIVec[iType][7],m_MyPAIVec[iType][8],m_MyPAIVec[iType][9],m_MyPAIVec[iType][10])&&CheckAAPai(m_MyPAIVec[iType][0],m_MyPAIVec[iType][1])) 
     { 
      return true; 
     } 
     return false; 
    } 
    if(iSize2==12) 
    { 
     //������ѹ 
     if(CheckAAABBBCCCPai(m_MyPAIVec[iType][0],m_MyPAIVec[iType][1],m_MyPAIVec[iType][2],m_MyPAIVec[iType][3],m_MyPAIVec[iType][4],m_MyPAIVec[iType][5],m_MyPAIVec[iType][6],m_MyPAIVec[iType][7],m_MyPAIVec[iType][8])&&Check3Pai(m_MyPAIVec[iType][9],m_MyPAIVec[iType][10],m_MyPAIVec[iType][11])) 
     { 
      return CheckHU(); 
     } 
     //������ѹ 
     if(CheckAAABBBCCCPai(m_MyPAIVec[iType][3],m_MyPAIVec[iType][4],m_MyPAIVec[iType][5],m_MyPAIVec[iType][6],m_MyPAIVec[iType][7],m_MyPAIVec[iType][8],m_MyPAIVec[iType][9],m_MyPAIVec[iType][10],m_MyPAIVec[iType][11])&&Check3Pai(m_MyPAIVec[iType][0],m_MyPAIVec[iType][1],m_MyPAIVec[iType][2])) 
     { 
      return CheckHU(); 
     }  
     return false; 
    } 
    if(iSize2==14) 
    { 
     //����˳��ǰ�� 
     if(CheckAAABBBCCCPai(m_MyPAIVec[iType][0],m_MyPAIVec[iType][1],m_MyPAIVec[iType][2],m_MyPAIVec[iType][3],m_MyPAIVec[iType][4],m_MyPAIVec[iType][5],m_MyPAIVec[iType][6],m_MyPAIVec[iType][7],m_MyPAIVec[iType][8])&&Check5Pai(m_MyPAIVec[iType][9],m_MyPAIVec[iType][10],m_MyPAIVec[iType][11],m_MyPAIVec[iType][12],m_MyPAIVec[iType][13])) 
     { 
      return true; 
     } 
     //����˳(��) 
     if(CheckAAPai(m_MyPAIVec[iType][0],m_MyPAIVec[iType][1])&&CheckAAABBBCCCPai(m_MyPAIVec[iType][2],m_MyPAIVec[iType][3],m_MyPAIVec[iType][4],m_MyPAIVec[iType][5],m_MyPAIVec[iType][6],m_MyPAIVec[iType][7],m_MyPAIVec[iType][8],m_MyPAIVec[iType][9],m_MyPAIVec[iType][10])&&Check3Pai(m_MyPAIVec[iType][11],m_MyPAIVec[iType][12],m_MyPAIVec[iType][13])) 
     { 
      return true; 
     }  
     //����˳(��) 
     if(Check3Pai(m_MyPAIVec[iType][0],m_MyPAIVec[iType][1],m_MyPAIVec[iType][2])&&CheckAAABBBCCCPai(m_MyPAIVec[iType][3],m_MyPAIVec[iType][4],m_MyPAIVec[iType][5],m_MyPAIVec[iType][6],m_MyPAIVec[iType][7],m_MyPAIVec[iType][8],m_MyPAIVec[iType][9],m_MyPAIVec[iType][10],m_MyPAIVec[iType][11])&&CheckAAPai(m_MyPAIVec[iType][12],m_MyPAIVec[iType][13])) 
     { 
      return true; 
     }  
     //����˳���� 
     if(CheckAAABBBCCCPai(m_MyPAIVec[iType][5],m_MyPAIVec[iType][6],m_MyPAIVec[iType][7],m_MyPAIVec[iType][8],m_MyPAIVec[iType][9],m_MyPAIVec[iType][10],m_MyPAIVec[iType][11],m_MyPAIVec[iType][12],m_MyPAIVec[iType][13])&&Check5Pai(m_MyPAIVec[iType][0],m_MyPAIVec[iType][1],m_MyPAIVec[iType][2],m_MyPAIVec[iType][3],m_MyPAIVec[iType][4])) 
     { 
      return true; 
     } 
     return false; 
    } 
   } 
   //�Ե�һ��˳ 
   if(iSize1==3) 
   { 
    if(iSize2==6) 
    { 
     //������ 
     if(CheckAABBCCPai(m_MyPAIVec[iType][0],m_MyPAIVec[iType][1],m_MyPAIVec[iType][2],m_MyPAIVec[iType][3],m_MyPAIVec[iType][4],m_MyPAIVec[iType][5])) 
     { 
      if(m_ChiPAIVec[iType][0]==m_MyPAIVec[iType][0]&&m_ChiPAIVec[iType][1]==m_MyPAIVec[iType][1]&&m_ChiPAIVec[iType][2]==m_MyPAIVec[iType][2]) 
      { 
       return CheckHU(); 
      } 
     } 
    } 
    if(iSize2==8) 
    { 
     //�����ԣ�ǰ�� 
     if(CheckAABBCCPai(m_MyPAIVec[iType][0],m_MyPAIVec[iType][1],m_MyPAIVec[iType][2],m_MyPAIVec[iType][3],m_MyPAIVec[iType][4],m_MyPAIVec[iType][5])&&CheckAAPai(m_MyPAIVec[iType][6],m_MyPAIVec[iType][7])) 
     { 
      if(m_ChiPAIVec[iType][0]==m_MyPAIVec[iType][0]&&m_ChiPAIVec[iType][1]==m_MyPAIVec[iType][2]&&m_ChiPAIVec[iType][2]==m_MyPAIVec[iType][4]) 
      { 
       return true; 
      } 
     } 
     //�����ԣ��� 
     if(CheckAABBCCPai(m_MyPAIVec[iType][2],m_MyPAIVec[iType][3],m_MyPAIVec[iType][4],m_MyPAIVec[iType][5],m_MyPAIVec[iType][6],m_MyPAIVec[iType][7])&&CheckAAPai(m_MyPAIVec[iType][0],m_MyPAIVec[iType][1])) 
     { 
      if(m_ChiPAIVec[iType][0]==m_MyPAIVec[iType][2]&&m_ChiPAIVec[iType][1]==m_MyPAIVec[iType][4]&&m_ChiPAIVec[iType][2]==m_MyPAIVec[iType][6]) 
      { 
       return true; 
      } 
     } 
    } 
    if(iSize2==9) 
    { 
     //�����ԣ�ǰ�� 
     if(CheckAABBCCPai(m_MyPAIVec[iType][0],m_MyPAIVec[iType][1],m_MyPAIVec[iType][2],m_MyPAIVec[iType][3],m_MyPAIVec[iType][4],m_MyPAIVec[iType][5])&&Check3Pai(m_MyPAIVec[iType][6],m_MyPAIVec[iType][7],m_MyPAIVec[iType][8])) 
     { 
      if(m_ChiPAIVec[iType][0]==m_MyPAIVec[iType][0]&&m_ChiPAIVec[iType][1]==m_MyPAIVec[iType][2]&&m_ChiPAIVec[iType][2]==m_MyPAIVec[iType][4]) 
      { 
       return CheckHU(); 
      } 
     } 
     //�����ԣ��� 
     if(CheckAABBCCPai(m_MyPAIVec[iType][3],m_MyPAIVec[iType][4],m_MyPAIVec[iType][5],m_MyPAIVec[iType][6],m_MyPAIVec[iType][7],m_MyPAIVec[iType][8])&&Check3Pai(m_MyPAIVec[iType][0],m_MyPAIVec[iType][1],m_MyPAIVec[iType][2])) 
     { 
      if(m_ChiPAIVec[iType][0]==m_MyPAIVec[iType][3]&&m_ChiPAIVec[iType][1]==m_MyPAIVec[iType][5]&&m_ChiPAIVec[iType][2]==m_MyPAIVec[iType][7]) 
      { 
       return CheckHU(); 
      } 
     } 
    } 
    if(iSize2==11) 
    { 
     //�����ԣ�ǰ�� 
     if(CheckAABBCCPai(m_MyPAIVec[iType][0],m_MyPAIVec[iType][1],m_MyPAIVec[iType][2],m_MyPAIVec[iType][3],m_MyPAIVec[iType][4],m_MyPAIVec[iType][5])&&Check5Pai(m_MyPAIVec[iType][6],m_MyPAIVec[iType][7],m_MyPAIVec[iType][8],m_MyPAIVec[iType][9],m_MyPAIVec[iType][10])) 
     { 
      if(m_ChiPAIVec[iType][0]==m_MyPAIVec[iType][0]&&m_ChiPAIVec[iType][1]==m_MyPAIVec[iType][2]&&m_ChiPAIVec[iType][2]==m_MyPAIVec[iType][4]) 
      { 
       return true; 
      } 
     } 
     //�����ԣ��У� 
     if(CheckAAPai(m_MyPAIVec[iType][0],m_MyPAIVec[iType][1])&&CheckAABBCCPai(m_MyPAIVec[iType][2],m_MyPAIVec[iType][3],m_MyPAIVec[iType][4],m_MyPAIVec[iType][5],m_MyPAIVec[iType][6],m_MyPAIVec[iType][7])&&Check3Pai(m_MyPAIVec[iType][8],m_MyPAIVec[iType][9],m_MyPAIVec[iType][10])) 
     { 
      if(m_ChiPAIVec[iType][0]==m_MyPAIVec[iType][2]&&m_ChiPAIVec[iType][1]==m_MyPAIVec[iType][4]&&m_ChiPAIVec[iType][2]==m_MyPAIVec[iType][6]) 
      { 
       return true; 
      } 
     } 
     //�����ԣ��У� 
     if(Check3Pai(m_MyPAIVec[iType][0],m_MyPAIVec[iType][1],m_MyPAIVec[iType][2])&&CheckAABBCCPai(m_MyPAIVec[iType][3],m_MyPAIVec[iType][4],m_MyPAIVec[iType][5],m_MyPAIVec[iType][6],m_MyPAIVec[iType][7],m_MyPAIVec[iType][8])&&CheckAAPai(m_MyPAIVec[iType][9],m_MyPAIVec[iType][10])) 
     { 
      if(m_ChiPAIVec[iType][0]==m_MyPAIVec[iType][3]&&m_ChiPAIVec[iType][1]==m_MyPAIVec[iType][5]&&m_ChiPAIVec[iType][2]==m_MyPAIVec[iType][7]) 
      { 
       return true; 
      } 
     } 
     //�����ԣ�ǰ�� 
     if(CheckAABBCCPai(m_MyPAIVec[iType][5],m_MyPAIVec[iType][6],m_MyPAIVec[iType][7],m_MyPAIVec[iType][8],m_MyPAIVec[iType][9],m_MyPAIVec[iType][10])&&Check5Pai(m_MyPAIVec[iType][0],m_MyPAIVec[iType][1],m_MyPAIVec[iType][2],m_MyPAIVec[iType][3],m_MyPAIVec[iType][4])) 
     { 
      if(m_ChiPAIVec[iType][0]==m_MyPAIVec[iType][5]&&m_ChiPAIVec[iType][1]==m_MyPAIVec[iType][7]&&m_ChiPAIVec[iType][2]==m_MyPAIVec[iType][9]) 
      { 
       return true; 
      } 
     } 
    } 
   } 
   //�Ե�����˳ 
   if(iSize1==6) 
   { 
    if(iSize2==3) 
    { 
     //˳�� 
     if(CheckABCPai(m_MyPAIVec[iType][0],m_MyPAIVec[iType][1],m_MyPAIVec[iType][2])) 
     { 
      if(m_ChiPAIVec[iType][0]==m_MyPAIVec[iType][0]&&m_ChiPAIVec[iType][1]==m_MyPAIVec[iType][1]&&m_ChiPAIVec[iType][2]==m_MyPAIVec[iType][2]) 
      { 
       if(m_ChiPAIVec[iType][3]==m_MyPAIVec[iType][0]&&m_ChiPAIVec[iType][4]==m_MyPAIVec[iType][1]&&m_ChiPAIVec[iType][5]==m_MyPAIVec[iType][2]) 
       { 
        return CheckHU(); 
       } 
      } 
     } 
    } 
    if(iSize2==5) 
    { 
     //˳�ӣ�ǰ�� 
     if(CheckABCPai(m_MyPAIVec[iType][0],m_MyPAIVec[iType][1],m_MyPAIVec[iType][2])&&CheckAAPai(m_MyPAIVec[iType][3],m_MyPAIVec[iType][4])) 
     { 
      if(m_ChiPAIVec[iType][0]==m_MyPAIVec[iType][0]&&m_ChiPAIVec[iType][1]==m_MyPAIVec[iType][1]&&m_ChiPAIVec[iType][2]==m_MyPAIVec[iType][2]) 
      { 
       if(m_ChiPAIVec[iType][3]==m_MyPAIVec[iType][0]&&m_ChiPAIVec[iType][4]==m_MyPAIVec[iType][1]&&m_ChiPAIVec[iType][5]==m_MyPAIVec[iType][2]) 
       { 
        return true; 
       } 
      } 
     } 
     //˳�ӣ��� 
     if(CheckABCPai(m_MyPAIVec[iType][2],m_MyPAIVec[iType][3],m_MyPAIVec[iType][4])&&CheckAAPai(m_MyPAIVec[iType][0],m_MyPAIVec[iType][1])) 
     { 
      if(m_ChiPAIVec[iType][0]==m_MyPAIVec[iType][2]&&m_ChiPAIVec[iType][1]==m_MyPAIVec[iType][3]&&m_ChiPAIVec[iType][2]==m_MyPAIVec[iType][4]) 
      { 
       if(m_ChiPAIVec[iType][3]==m_MyPAIVec[iType][2]&&m_ChiPAIVec[iType][4]==m_MyPAIVec[iType][3]&&m_ChiPAIVec[iType][5]==m_MyPAIVec[iType][4]) 
       { 
        return true; 
       } 
      } 
     } 
    } 
    if(iSize2==6) 
    { 
     //������ 
     if(CheckAABBCCPai(m_MyPAIVec[iType][0],m_MyPAIVec[iType][1],m_MyPAIVec[iType][2],m_MyPAIVec[iType][3],m_MyPAIVec[iType][4],m_MyPAIVec[iType][5])) 
     { 
      if(m_ChiPAIVec[iType][0]==m_MyPAIVec[iType][0]&&m_ChiPAIVec[iType][1]==m_MyPAIVec[iType][2]&&m_ChiPAIVec[iType][2]==m_MyPAIVec[iType][4]) 
      { 
       if(m_ChiPAIVec[iType][3]==m_MyPAIVec[iType][1]&&m_ChiPAIVec[iType][4]==m_MyPAIVec[iType][3]&&m_ChiPAIVec[iType][5]==m_MyPAIVec[iType][5]) 
       { 
        return CheckHU(); 
       } 
      } 
     } 
    } 
    if(iSize2==8) 
    { 
     //������(ǰ) 
     if(CheckAABBCCPai(m_MyPAIVec[iType][0],m_MyPAIVec[iType][1],m_MyPAIVec[iType][2],m_MyPAIVec[iType][3],m_MyPAIVec[iType][4],m_MyPAIVec[iType][5])&&CheckAAPai(m_MyPAIVec[iType][6],m_MyPAIVec[iType][7])) 
     { 
      if(m_ChiPAIVec[iType][0]==m_MyPAIVec[iType][0]&&m_ChiPAIVec[iType][1]==m_MyPAIVec[iType][2]&&m_ChiPAIVec[iType][2]==m_MyPAIVec[iType][4]) 
      { 
       if(m_ChiPAIVec[iType][3]==m_MyPAIVec[iType][1]&&m_ChiPAIVec[iType][4]==m_MyPAIVec[iType][3]&&m_ChiPAIVec[iType][5]==m_MyPAIVec[iType][5]) 
       { 
        return true; 
       } 
      } 
     } 
     //������(��) 
     if(CheckAABBCCPai(m_MyPAIVec[iType][2],m_MyPAIVec[iType][3],m_MyPAIVec[iType][4],m_MyPAIVec[iType][5],m_MyPAIVec[iType][6],m_MyPAIVec[iType][7])&&CheckAAPai(m_MyPAIVec[iType][0],m_MyPAIVec[iType][1])) 
     { 
      if(m_ChiPAIVec[iType][0]==m_MyPAIVec[iType][2]&&m_ChiPAIVec[iType][1]==m_MyPAIVec[iType][4]&&m_ChiPAIVec[iType][2]==m_MyPAIVec[iType][6]) 
      { 
       if(m_ChiPAIVec[iType][3]==m_MyPAIVec[iType][3]&&m_ChiPAIVec[iType][4]==m_MyPAIVec[iType][5]&&m_ChiPAIVec[iType][5]==m_MyPAIVec[iType][7]) 
       { 
        return true; 
       } 
      } 
     } 
    } 
   } 
   //�Ե�����˳ 
   if(iSize1==9) 
   { 
    if((m_ChiPAIVec[2][0]==m_ChiPAIVec[iType][3])&&(m_ChiPAIVec[iType][3]==m_ChiPAIVec[iType][6])) 
    { 
     return CheckHU(); 
    } 
   } 
  } 
 } 
 return false; 
} 
//����Ƿ�һɫ���ڸ� 
bool CMJ::Check1S3JG_HU() 
{ 
 //�������� 
 for(UINT i = 2 ; i <= 4 ; i++) 
 { 
  int iType = i; 
  if(m_GangPAIVec[iType].size()==12) 
  { 
   if((m_GangPAIVec[iType][0]==m_GangPAIVec[iType][4]-1)&&(m_GangPAIVec[iType][4]==m_GangPAIVec[iType][8]-1)) 
   { 
    return CheckHU(); 
   } 
  } 
 } 
 return false; 
} 
//����Ƿ�ȫ�� 
bool CMJ::CheckQD_HU() 
{ 
 //���ƣ����� 
 if(m_MyPAIVec[0].empty()==false)return false; 
 if(m_MyPAIVec[1].empty()==false)return false; 
 if(m_ChiPAIVec[0].empty()==false)return false; 
 if(m_ChiPAIVec[1].empty()==false)return false; 
 if(m_PengPAIVec[0].empty()==false)return false; 
 if(m_PengPAIVec[1].empty()==false)return false; 
 if(m_GangPAIVec[0].empty()==false)return false; 
 if(m_GangPAIVec[1].empty()==false)return false; 
   
 //�������� 
 for(UINT i = 2 ; i <= 4 ; i++ ) 
 { 
  if(m_MyPAIVec[i].empty()==false) 
  { 
   //ʣ����ǽ 
   int iSize = m_MyPAIVec[i].size(); 
   for( UINT j = 0 ; j < iSize ; j++ ) 
   { 
    if(m_MyPAIVec[i][j]<7)return false; 
   } 
   //�� 
   iSize = m_ChiPAIVec[i].size(); 
   for( UINT j = 0 ; j < iSize ; j++ ) 
   { 
    if(m_ChiPAIVec[i][j]<7)return false; 
   } 
   //�� 
   iSize = m_PengPAIVec[i].size(); 
   for( UINT j = 0 ; j < iSize ; j++ ) 
   { 
    if(m_PengPAIVec[i][j]<7)return false; 
   } 
   //�� 
   iSize = m_GangPAIVec[i].size(); 
   for( UINT j = 0 ; j < iSize ; j++ ) 
   { 
    if(m_GangPAIVec[i][j]<7)return false; 
   } 
  } 
 } 
 return CheckHU(); 
} 
  
//����Ƿ�ȫ�� 
bool CMJ::CheckQZ_HU() 
{ 
//���ƣ����� 
 if(m_MyPAIVec[0].empty()==false)return false; 
 if(m_MyPAIVec[1].empty()==false)return false; 
 if(m_ChiPAIVec[0].empty()==false)return false; 
 if(m_ChiPAIVec[1].empty()==false)return false; 
 if(m_PengPAIVec[0].empty()==false)return false; 
 if(m_PengPAIVec[1].empty()==false)return false; 
 if(m_GangPAIVec[0].empty()==false)return false; 
 if(m_GangPAIVec[1].empty()==false)return false; 
   
 //�������� 
 for(UINT i = 2 ; i <= 4 ; i++ ) 
 { 
  if(m_MyPAIVec[i].empty()==false) 
  { 
   //ʣ����ǽ 
   int iSize = m_MyPAIVec[i].size(); 
   for( UINT j = 0 ; j < iSize ; j++ ) 
   { 
    if(m_MyPAIVec[i][j]<4)return false; 
    if(m_MyPAIVec[i][j]>6)return false; 
   } 
   //�� 
   iSize = m_ChiPAIVec[i].size(); 
   for( UINT j = 0 ; j < iSize ; j++ ) 
   { 
    if(m_ChiPAIVec[i][j]<4)return false; 
    if(m_ChiPAIVec[i][j]>6)return false; 
   } 
   //�� 
   iSize = m_PengPAIVec[i].size(); 
   for( UINT j = 0 ; j < iSize ; j++ ) 
   { 
    if(m_PengPAIVec[i][j]<4)return false; 
    if(m_PengPAIVec[i][j]>6)return false; 
   } 
   //�� 
   iSize = m_GangPAIVec[i].size(); 
   for( UINT j = 0 ; j < iSize ; j++ ) 
   { 
    if(m_GangPAIVec[i][j]<4)return false; 
    if(m_GangPAIVec[i][j]>6)return false; 
   } 
  } 
 } 
 return CheckHU(); 
} 
  
//����Ƿ�ȫС 
bool CMJ::CheckQX_HU() 
{ 
 //���ƣ����� 
 if(m_MyPAIVec[0].empty()==false)return false; 
 if(m_MyPAIVec[1].empty()==false)return false; 
 if(m_ChiPAIVec[0].empty()==false)return false; 
 if(m_ChiPAIVec[1].empty()==false)return false; 
 if(m_PengPAIVec[0].empty()==false)return false; 
 if(m_PengPAIVec[1].empty()==false)return false; 
 if(m_GangPAIVec[0].empty()==false)return false; 
 if(m_GangPAIVec[1].empty()==false)return false; 
   
 //�������� 
 for(UINT i = 2 ; i <= 4 ; i++ ) 
 { 
  if(m_MyPAIVec[i].empty()==false) 
  { 
   //ʣ����ǽ 
   int iSize = m_MyPAIVec[i].size(); 
   for( UINT j = 0 ; j < iSize ; j++ ) 
   { 
    if(m_MyPAIVec[i][j]>3)return false; 
   } 
   //�� 
   iSize = m_ChiPAIVec[i].size(); 
   for( UINT j = 0 ; j < iSize ; j++ ) 
   { 
    if(m_ChiPAIVec[i][j]>3)return false; 
   } 
   //�� 
   iSize = m_PengPAIVec[i].size(); 
   for( UINT j = 0 ; j < iSize ; j++ ) 
   { 
    if(m_PengPAIVec[i][j]>3)return false; 
   } 
   //�� 
   iSize = m_GangPAIVec[i].size(); 
   for( UINT j = 0 ; j < iSize ; j++ ) 
   { 
    if(m_GangPAIVec[i][j]>3)return false; 
   } 
  } 
 } 
 return CheckHU(); 
} 
//����Ƿ����� 
bool CMJ::CheckQL_HU() 
{ 
 //��ɫ 
 int iColorNum = 0; 
 //�������� 
 for(UINT i = 2 ; i <= 4 ; i++ ) 
 { 
  if(m_MyPAIVec[i].empty()==false) 
  { 
   iColorNum++; 
  
   if(m_MyPAIVec[i].size()==9) 
   { 
    for(UINT j = 0 ;j < 9 ;j++) 
    { 
     if(m_MyPAIVec[i][j] != j)return false; 
    } 
   } 
  } 
 } 
 if(iColorNum==1)return CheckHU(); 
 return false; 
} 
//����Ƿ���ɫ˫���� 
bool CMJ::Check3S2LH_HU() 
{ 
 //����Ϊ˫�� 
 if(m_MyPAIVec[2].size()==2) 
 { 
  //˫�� 
  if(m_MyPAIVec[2][0]==5&&m_MyPAIVec[2][1]==5) 
  { 
   //���ٸ� 
   if(m_MyPAIVec[3].size()==6&&m_MyPAIVec[4].size()==6) 
   { 
    if(m_MyPAIVec[3][0]==1&&m_MyPAIVec[3][1]==2&&m_MyPAIVec[3][2]==3&&m_MyPAIVec[3][3]==7&&m_MyPAIVec[3][4]==8&&m_MyPAIVec[3][5]==9) 
    { 
     if(m_MyPAIVec[4][0]==1&&m_MyPAIVec[4][1]==2&&m_MyPAIVec[4][2]==3&&m_MyPAIVec[4][3]==7&&m_MyPAIVec[4][4]==8&&m_MyPAIVec[4][5]==9) 
     { 
      return true; 
     } 
    } 
   } 
  } 
 } 
  
 //����Ϊ˫�� 
 if(m_MyPAIVec[3].size()==2) 
 { 
  //˫�� 
  if(m_MyPAIVec[3][0]==5&&m_MyPAIVec[3][1]==5) 
  { 
   //���ٸ� 
   if(m_MyPAIVec[2].size()==6&&m_MyPAIVec[4].size()==6) 
   { 
    if(m_MyPAIVec[2][0]==1&&m_MyPAIVec[2][1]==2&&m_MyPAIVec[2][2]==3&&m_MyPAIVec[2][3]==7&&m_MyPAIVec[2][4]==8&&m_MyPAIVec[2][5]==9) 
    { 
     if(m_MyPAIVec[4][0]==1&&m_MyPAIVec[4][1]==2&&m_MyPAIVec[4][2]==3&&m_MyPAIVec[4][3]==7&&m_MyPAIVec[4][4]==8&&m_MyPAIVec[4][5]==9) 
     { 
      return true; 
     } 
    } 
   } 
  } 
 } 
  
 //���Ϊ˫�� 
 if(m_MyPAIVec[4].size()==2) 
 { 
  //˫�� 
  if(m_MyPAIVec[4][0]==5&&m_MyPAIVec[4][1]==5) 
  { 
   //���ٸ� 
   if(m_MyPAIVec[2].size()==6&&m_MyPAIVec[3].size()==6) 
   { 
    if(m_MyPAIVec[2][0]==1&&m_MyPAIVec[2][1]==2&&m_MyPAIVec[2][2]==3&&m_MyPAIVec[2][3]==7&&m_MyPAIVec[2][4]==8&&m_MyPAIVec[2][5]==9) 
    { 
     if(m_MyPAIVec[3][0]==1&&m_MyPAIVec[3][1]==2&&m_MyPAIVec[3][2]==3&&m_MyPAIVec[3][3]==7&&m_MyPAIVec[3][4]==8&&m_MyPAIVec[3][5]==9) 
     { 
      return true; 
     } 
    } 
   } 
  } 
 } 
 return false; 
} 
  
//����Ƿ�һɫ������ 
bool CMJ::Check1S3BG_HU() 
{ 
 return false; 
} 
//ȫ���� 
bool CMJ::CheckQD5_HU() 
{ 
 //���ƣ����� 
 if(m_MyPAIVec[0].empty()==false)return false; 
 if(m_MyPAIVec[1].empty()==false)return false; 
 if(m_ChiPAIVec[0].empty()==false)return false; 
 if(m_ChiPAIVec[1].empty()==false)return false; 
 if(m_PengPAIVec[0].empty()==false)return false; 
 if(m_PengPAIVec[1].empty()==false)return false; 
 if(m_GangPAIVec[0].empty()==false)return false; 
 if(m_GangPAIVec[1].empty()==false)return false; 
 return false; 
} 
//��ͬ�� 
bool CMJ::Check3TK_HU() 
{ 
 /*if(m_GangPAIVec[2].size()==4) 
 { 
  //�������� 
  for(UINT i = 3 ; i <= 4 ; i++ ) 
  { 
   if(m_GangPAIVec[i].size()==4) 
   { 
    if(m_GangPAIVec[2][0]!=m_GangPAIVec[i][0]) 
    { 
     return false; 
    } 
   } 
  }  
 }*/
 return false; 
  
} 
//������ 
bool CMJ::Check3AK_HU() 
{ 
 return false; 
} 
//������ 
bool CMJ::CheckDDJ_HU() 
{ 
 int count = 0; 
 for(UINT i = 0 ; i < 6 ; i++ ) 
 { 
  count += m_MyPAIVec[i].size(); 
 } 
 if(count==2) 
 { 
  if(m_MyPAIVec[m_LastPAI.m_Type].size()==2) 
  { 
   if(m_MyPAIVec[m_LastPAI.m_Type][0]==m_MyPAIVec[m_LastPAI.m_Type][1])return true; 
  } 
 } 
 return false; 
} 
//����Ƿ���ʮ���� 
bool CMJ::Check13Y_TING() 
{ 
 bool  i13YSize[13] ; 
 for(UINT i = 0 ; i < 13 ; i++ ) 
 { 
  i13YSize[i]=false; 
 } 
 //�з��� 
 vector<int>::iterator Iter; 
 for(Iter = m_MyPAIVec[0].begin();Iter != m_MyPAIVec[0].end(); Iter++ ) 
 { 
  if((*Iter)==1) 
  { 
   i13YSize[0]=true; 
  } 
  if((*Iter)==2) 
  { 
   i13YSize[1]=true; 
  } 
  if((*Iter)==3) 
  { 
   i13YSize[2]=true; 
  } 
 } 
 //���������� 
 for(Iter = m_MyPAIVec[1].begin();Iter != m_MyPAIVec[1].end(); Iter++ ) 
 { 
  if((*Iter)==1) 
  { 
   i13YSize[3]=true; 
  } 
  if((*Iter)==2) 
  { 
   i13YSize[4]=true; 
  } 
  if((*Iter)==3) 
  { 
   i13YSize[5]=true; 
  } 
  if((*Iter)==4) 
  { 
   i13YSize[6]=true; 
  } 
 } 
 //һ���� 
 for(Iter = m_MyPAIVec[2].begin();Iter != m_MyPAIVec[2].end(); Iter++ ) 
 { 
  if((*Iter)==1) 
  { 
   i13YSize[7]=true; 
  } 
  if((*Iter)==9) 
  { 
   i13YSize[8]=true; 
  } 
 } 
  
 //һ���� 
 for(Iter = m_MyPAIVec[3].begin();Iter != m_MyPAIVec[3].end(); Iter++ ) 
 { 
  if((*Iter)==1) 
  { 
   i13YSize[9]=true; 
  } 
  if((*Iter)==9) 
  { 
   i13YSize[10]=true; 
  } 
 } 
   
 //һ�ű� 
 for(Iter = m_MyPAIVec[4].begin();Iter != m_MyPAIVec[4].end(); Iter++ ) 
 { 
  if((*Iter)==1) 
  { 
   i13YSize[11]=true; 
  } 
  if((*Iter)==9) 
  { 
   i13YSize[12]=true; 
  } 
 } 
 int icount = 0; 
 for(UINT i = 0 ; i < 13 ; i++ ) 
 { 
  if(i13YSize[i]==true) 
  { 
   icount++; 
  } 
 } 
 if(icount >=12)return true; 
 return false; 
} 
//����Ƿ����İ��� 
bool CMJ::Check4AK_TING() 
{ 
 if(m_AKNum==4)return true; 
 return false; 
} 
//���� 
bool CMJ::CheckHU() 
{ 
 bool t_Ok = false; 
 int iJiangNum = 0; 
  
 int iSize = m_MyPAIVec[0].size(); 
 if(iSize>0) 
 { 
  //�з��� 
  if(iSize==2) 
  { 
   if(!CheckAAPai(m_MyPAIVec[0][0],m_MyPAIVec[0][1])) 
   { 
    return false; 
   } 
   else
   { 
    iJiangNum++ ; 
   } 
  } 
  else if(iSize==3) 
  { 
   if(!CheckAAAPai(m_MyPAIVec[0][0],m_MyPAIVec[0][1],m_MyPAIVec[0][2])) 
   { 
    return false; 
   } 
  } 
  else if(iSize==5) 
  { 
   if(CheckAAPai(m_MyPAIVec[0][0],m_MyPAIVec[0][1])&&CheckAAAPai(m_MyPAIVec[0][2],m_MyPAIVec[0][3],m_MyPAIVec[0][4])) 
   { 
    iJiangNum++ ; 
   } 
   else if(CheckAAAPai(m_MyPAIVec[0][0],m_MyPAIVec[0][1],m_MyPAIVec[0][2])&&CheckAAPai(m_MyPAIVec[0][3],m_MyPAIVec[0][4])) 
   { 
    iJiangNum++ ; 
   } 
   else
   { 
    return false; 
   } 
  } 
  else if(iSize==8) 
  { 
   if(CheckAAPai(m_MyPAIVec[0][0],m_MyPAIVec[0][1])&&CheckAAAPai(m_MyPAIVec[0][2],m_MyPAIVec[0][3],m_MyPAIVec[0][4])&&CheckAAAPai(m_MyPAIVec[0][5],m_MyPAIVec[0][6],m_MyPAIVec[0][7])) 
   { 
    iJiangNum++ ; 
   } 
   else if(CheckAAAPai(m_MyPAIVec[0][0],m_MyPAIVec[0][1],m_MyPAIVec[0][2])&&CheckAAPai(m_MyPAIVec[0][3],m_MyPAIVec[0][4])&&CheckAAAPai(m_MyPAIVec[0][5],m_MyPAIVec[0][6],m_MyPAIVec[0][7])) 
   { 
    iJiangNum++ ; 
   } 
   else if(CheckAAAPai(m_MyPAIVec[0][0],m_MyPAIVec[0][1],m_MyPAIVec[0][2])&&CheckAAAPai(m_MyPAIVec[0][3],m_MyPAIVec[0][4],m_MyPAIVec[0][5])&&CheckAAPai(m_MyPAIVec[0][6],m_MyPAIVec[0][7])) 
   { 
    iJiangNum++ ; 
   } 
   else
   { 
    return false; 
   } 
  } 
  else if(iSize==11) 
  { 
   if(CheckAAPai(m_MyPAIVec[0][0],m_MyPAIVec[0][1])&&CheckAAAPai(m_MyPAIVec[0][2],m_MyPAIVec[0][3],m_MyPAIVec[0][4])&&CheckAAAPai(m_MyPAIVec[0][5],m_MyPAIVec[0][6],m_MyPAIVec[0][7])&&CheckAAAPai(m_MyPAIVec[0][8],m_MyPAIVec[0][9],m_MyPAIVec[0][10])) 
   { 
    iJiangNum++ ; 
   } 
   else if(CheckAAAPai(m_MyPAIVec[0][0],m_MyPAIVec[0][1],m_MyPAIVec[0][2])&&CheckAAPai(m_MyPAIVec[0][3],m_MyPAIVec[0][4])&&CheckAAAPai(m_MyPAIVec[0][5],m_MyPAIVec[0][6],m_MyPAIVec[0][7])&&CheckAAAPai(m_MyPAIVec[0][8],m_MyPAIVec[0][9],m_MyPAIVec[0][10])) 
   { 
    iJiangNum++ ; 
   } 
   else if(CheckAAAPai(m_MyPAIVec[0][0],m_MyPAIVec[0][1],m_MyPAIVec[0][2])&&CheckAAAPai(m_MyPAIVec[0][3],m_MyPAIVec[0][4],m_MyPAIVec[0][5])&&CheckAAPai(m_MyPAIVec[0][6],m_MyPAIVec[0][7])&&CheckAAAPai(m_MyPAIVec[0][8],m_MyPAIVec[0][9],m_MyPAIVec[0][10])) 
   { 
    iJiangNum++ ; 
   } 
   else if(CheckAAAPai(m_MyPAIVec[0][0],m_MyPAIVec[0][1],m_MyPAIVec[0][2])&&CheckAAAPai(m_MyPAIVec[0][3],m_MyPAIVec[0][4],m_MyPAIVec[0][5])&&CheckAAAPai(m_MyPAIVec[0][6],m_MyPAIVec[0][7],m_MyPAIVec[0][8])&&CheckAAPai(m_MyPAIVec[0][9],m_MyPAIVec[0][10])) 
   { 
    iJiangNum++ ; 
   } 
   else
   { 
    return false; 
   } 
  } 
  else
  { 
   return false; 
  } 
  
 } 
 //�������� 
 iSize = m_MyPAIVec[1].size(); 
 if(iSize>0) 
 { 
  if(iSize==2) 
  { 
   if(!CheckAAPai(m_MyPAIVec[1][0],m_MyPAIVec[1][1])) 
   { 
    return false; 
   } 
   else
   { 
    iJiangNum++ ; 
   } 
  } 
  else if(iSize==3) 
  { 
   if(!CheckAAAPai(m_MyPAIVec[1][0],m_MyPAIVec[1][1],m_MyPAIVec[1][2])) 
   { 
    return false; 
   }  
  } 
  else if(iSize==5) 
  { 
   if(CheckAAPai(m_MyPAIVec[1][0],m_MyPAIVec[1][1])&&CheckAAAPai(m_MyPAIVec[1][2],m_MyPAIVec[1][3],m_MyPAIVec[1][4])) 
   { 
    iJiangNum++ ; 
   } 
   else if(CheckAAAPai(m_MyPAIVec[1][0],m_MyPAIVec[1][1],m_MyPAIVec[1][2])&&CheckAAPai(m_MyPAIVec[1][3],m_MyPAIVec[1][4])) 
   { 
    iJiangNum++ ; 
   } 
   else
   { 
    return false; 
   } 
  } 
  else if(iSize==8) 
  { 
   if(CheckAAPai(m_MyPAIVec[1][0],m_MyPAIVec[1][1])&&CheckAAAPai(m_MyPAIVec[1][2],m_MyPAIVec[1][3],m_MyPAIVec[1][4])&&CheckAAAPai(m_MyPAIVec[1][5],m_MyPAIVec[1][6],m_MyPAIVec[1][7])) 
   { 
    iJiangNum++ ; 
   } 
   else if(CheckAAAPai(m_MyPAIVec[1][0],m_MyPAIVec[1][1],m_MyPAIVec[1][2])&&CheckAAPai(m_MyPAIVec[1][3],m_MyPAIVec[1][4])&&CheckAAAPai(m_MyPAIVec[1][5],m_MyPAIVec[1][6],m_MyPAIVec[1][7])) 
   { 
    iJiangNum++ ; 
   } 
   else if(CheckAAAPai(m_MyPAIVec[1][0],m_MyPAIVec[1][1],m_MyPAIVec[1][2])&&CheckAAAPai(m_MyPAIVec[1][3],m_MyPAIVec[1][4],m_MyPAIVec[1][5])&&CheckAAPai(m_MyPAIVec[1][6],m_MyPAIVec[1][7])) 
   { 
    iJiangNum++ ; 
   } 
   else
   { 
    return false; 
   } 
  } 
  else if(iSize==11) 
  { 
   if(CheckAAPai(m_MyPAIVec[1][0],m_MyPAIVec[1][1])&&CheckAAAPai(m_MyPAIVec[1][2],m_MyPAIVec[1][3],m_MyPAIVec[1][4])&&CheckAAAPai(m_MyPAIVec[1][5],m_MyPAIVec[1][6],m_MyPAIVec[1][7])&&CheckAAAPai(m_MyPAIVec[1][8],m_MyPAIVec[1][9],m_MyPAIVec[1][10])) 
   { 
    iJiangNum++ ; 
   } 
   else if(CheckAAAPai(m_MyPAIVec[1][0],m_MyPAIVec[1][1],m_MyPAIVec[1][2])&&CheckAAPai(m_MyPAIVec[1][3],m_MyPAIVec[1][4])&&CheckAAAPai(m_MyPAIVec[1][5],m_MyPAIVec[1][6],m_MyPAIVec[1][7])&&CheckAAAPai(m_MyPAIVec[1][8],m_MyPAIVec[1][9],m_MyPAIVec[1][10])) 
   { 
    iJiangNum++ ; 
   } 
   else if(CheckAAAPai(m_MyPAIVec[1][0],m_MyPAIVec[1][1],m_MyPAIVec[1][2])&&CheckAAAPai(m_MyPAIVec[1][3],m_MyPAIVec[1][4],m_MyPAIVec[1][5])&&CheckAAPai(m_MyPAIVec[1][6],m_MyPAIVec[1][7])&&CheckAAAPai(m_MyPAIVec[1][8],m_MyPAIVec[1][9],m_MyPAIVec[1][10])) 
   { 
    iJiangNum++ ; 
   } 
   else if(CheckAAAPai(m_MyPAIVec[1][0],m_MyPAIVec[1][1],m_MyPAIVec[1][2])&&CheckAAAPai(m_MyPAIVec[1][3],m_MyPAIVec[1][4],m_MyPAIVec[1][5])&&CheckAAAPai(m_MyPAIVec[1][6],m_MyPAIVec[1][7],m_MyPAIVec[1][8])&&CheckAAPai(m_MyPAIVec[1][9],m_MyPAIVec[1][10])) 
   { 
    iJiangNum++ ; 
   } 
   else
   { 
    return false; 
   } 
  } 
  else
  { 
   return false; 
  } 
 } 
 //�� 
 iSize = m_MyPAIVec[2].size(); 
 if(iSize>0) 
 { 
  if(iSize==2) 
  { 
   if(!CheckAAPai(m_MyPAIVec[2][0],m_MyPAIVec[2][1])) 
   { 
    return false; 
   } 
   else
   { 
    iJiangNum++ ; 
   } 
  } 
  else if(iSize==3) 
  { 
   if(!CheckAAAPai(m_MyPAIVec[2][0],m_MyPAIVec[2][1],m_MyPAIVec[2][2])) 
   { 
    if(!CheckABCPai(m_MyPAIVec[2][0],m_MyPAIVec[2][1],m_MyPAIVec[2][2])) 
    { 
     return false; 
    } 
   } 
  } 
  else if(iSize==5) 
  { 
   if(!Check5Pai(m_MyPAIVec[2][0],m_MyPAIVec[2][1],m_MyPAIVec[2][2],m_MyPAIVec[2][3],m_MyPAIVec[2][4])) 
   { 
    return false; 
   } 
   else
   { 
    iJiangNum++ ; 
   } 
  } 
  else if(iSize==6) 
  { 
   if(!Check6Pai(m_MyPAIVec[2][0],m_MyPAIVec[2][1],m_MyPAIVec[2][2],m_MyPAIVec[2][3],m_MyPAIVec[2][4],m_MyPAIVec[2][5])) 
   { 
    return false; 
   } 
  } 
  else if(iSize==8) 
  { 
   if(!Check8Pai(m_MyPAIVec[2][0],m_MyPAIVec[2][1],m_MyPAIVec[2][2],m_MyPAIVec[2][3],m_MyPAIVec[2][4],m_MyPAIVec[2][5],m_MyPAIVec[2][6],m_MyPAIVec[2][7])) 
   { 
    return false; 
   } 
   else
   { 
    iJiangNum++ ; 
   } 
  } 
  else if(iSize==9) 
  { 
   if(!Check9Pai(m_MyPAIVec[2][0],m_MyPAIVec[2][1],m_MyPAIVec[2][2],m_MyPAIVec[2][3],m_MyPAIVec[2][4],m_MyPAIVec[2][5],m_MyPAIVec[2][6],m_MyPAIVec[2][7],m_MyPAIVec[2][8])) 
   { 
    return false; 
   } 
  } 
  else if(iSize==11) 
  { 
   if(!Check11Pai(m_MyPAIVec[2][0],m_MyPAIVec[2][1],m_MyPAIVec[2][2],m_MyPAIVec[2][3],m_MyPAIVec[2][4],m_MyPAIVec[2][5],m_MyPAIVec[2][6],m_MyPAIVec[2][7],m_MyPAIVec[2][8],m_MyPAIVec[2][9],m_MyPAIVec[2][10])) 
   { 
    return false; 
   } 
   else
   { 
    iJiangNum++ ; 
   } 
  } 
  else if(iSize==12) 
  { 
   if(!Check12Pai(m_MyPAIVec[2][0],m_MyPAIVec[2][1],m_MyPAIVec[2][2],m_MyPAIVec[2][3],m_MyPAIVec[2][4],m_MyPAIVec[2][5],m_MyPAIVec[2][6],m_MyPAIVec[2][7],m_MyPAIVec[2][8],m_MyPAIVec[2][9],m_MyPAIVec[2][10],m_MyPAIVec[2][11])) 
   { 
    return false; 
   } 
  } 
  else if(iSize==14) 
  { 
   if(!Check14Pai(m_MyPAIVec[2][0],m_MyPAIVec[2][1],m_MyPAIVec[2][2],m_MyPAIVec[2][3],m_MyPAIVec[2][4],m_MyPAIVec[2][5],m_MyPAIVec[2][6],m_MyPAIVec[2][7],m_MyPAIVec[2][8],m_MyPAIVec[2][9],m_MyPAIVec[2][10],m_MyPAIVec[2][11],m_MyPAIVec[2][12],m_MyPAIVec[2][13])) 
   { 
    return false; 
   } 
   else
   { 
    iJiangNum++ ; 
   } 
  } 
  else
  { 
   return false; 
  } 
 } 
  
 //�� 
 iSize = m_MyPAIVec[3].size(); 
 if(iSize>0) 
 { 
  if(iSize==2) 
  { 
   if(!CheckAAPai(m_MyPAIVec[3][0],m_MyPAIVec[3][1])) 
   { 
    return false; 
   } 
   else
   { 
    iJiangNum++ ; 
   } 
  } 
  else if(iSize==3) 
  { 
   if(!CheckAAAPai(m_MyPAIVec[3][0],m_MyPAIVec[3][1],m_MyPAIVec[3][2])) 
   { 
    if(!CheckABCPai(m_MyPAIVec[3][0],m_MyPAIVec[3][1],m_MyPAIVec[3][2])) 
    { 
     return false; 
    } 
   } 
  } 
  else if(iSize==5) 
  { 
   if(!Check5Pai(m_MyPAIVec[3][0],m_MyPAIVec[3][1],m_MyPAIVec[3][2],m_MyPAIVec[3][3],m_MyPAIVec[3][4])) 
   { 
    return false; 
   } 
   else
   { 
    iJiangNum++ ; 
   } 
  } 
  else if(iSize==6) 
  { 
   if(!Check6Pai(m_MyPAIVec[3][0],m_MyPAIVec[3][1],m_MyPAIVec[3][2],m_MyPAIVec[3][3],m_MyPAIVec[3][4],m_MyPAIVec[3][5])) 
   { 
    return false; 
   } 
  } 
  else if(iSize==8) 
  { 
   if(!Check8Pai(m_MyPAIVec[3][0],m_MyPAIVec[3][1],m_MyPAIVec[3][2],m_MyPAIVec[3][3],m_MyPAIVec[3][4],m_MyPAIVec[3][5],m_MyPAIVec[3][6],m_MyPAIVec[3][7])) 
   { 
    return false; 
   } 
   else
   { 
    iJiangNum++ ; 
   } 
  } 
  else if(iSize==9) 
  { 
   if(!Check9Pai(m_MyPAIVec[3][0],m_MyPAIVec[3][1],m_MyPAIVec[3][2],m_MyPAIVec[3][3],m_MyPAIVec[3][4],m_MyPAIVec[3][5],m_MyPAIVec[3][6],m_MyPAIVec[3][7],m_MyPAIVec[3][8])) 
   { 
    return false; 
   } 
  } 
  else if(iSize==11) 
  { 
   if(!Check11Pai(m_MyPAIVec[3][0],m_MyPAIVec[3][1],m_MyPAIVec[3][2],m_MyPAIVec[3][3],m_MyPAIVec[3][4],m_MyPAIVec[3][5],m_MyPAIVec[3][6],m_MyPAIVec[3][7],m_MyPAIVec[3][8],m_MyPAIVec[3][9],m_MyPAIVec[3][10])) 
   { 
    return false; 
   } 
   else
   { 
    iJiangNum++ ; 
   } 
  } 
  else if(iSize==12) 
  { 
   if(!Check12Pai(m_MyPAIVec[3][0],m_MyPAIVec[3][1],m_MyPAIVec[3][2],m_MyPAIVec[3][3],m_MyPAIVec[3][4],m_MyPAIVec[3][5],m_MyPAIVec[3][6],m_MyPAIVec[3][7],m_MyPAIVec[3][8],m_MyPAIVec[3][9],m_MyPAIVec[3][10],m_MyPAIVec[3][11])) 
   { 
    return false; 
   } 
  } 
  else if(iSize==14) 
  { 
   if(!Check14Pai(m_MyPAIVec[3][0],m_MyPAIVec[3][1],m_MyPAIVec[3][2],m_MyPAIVec[3][3],m_MyPAIVec[3][4],m_MyPAIVec[3][5],m_MyPAIVec[3][6],m_MyPAIVec[3][7],m_MyPAIVec[3][8],m_MyPAIVec[3][9],m_MyPAIVec[3][10],m_MyPAIVec[3][11],m_MyPAIVec[3][12],m_MyPAIVec[3][13])) 
   { 
    return false; 
   } 
   else
   { 
    iJiangNum++ ; 
   } 
  } 
  else
  { 
   return false; 
  } 
  
 } 
  
 //�� 
 iSize = m_MyPAIVec[4].size(); 
 if(iSize>0) 
 { 
  if(iSize==2) 
  { 
   if(!CheckAAPai(m_MyPAIVec[4][0],m_MyPAIVec[4][1])) 
   { 
    return false; 
   } 
   else
   { 
    iJiangNum++ ; 
   } 
  } 
  else if(iSize==3) 
  { 
   if(!CheckAAAPai(m_MyPAIVec[4][0],m_MyPAIVec[4][1],m_MyPAIVec[4][2])) 
   { 
    if(!CheckABCPai(m_MyPAIVec[4][0],m_MyPAIVec[4][1],m_MyPAIVec[4][2])) 
    { 
     return false; 
    } 
   } 
  } 
  else if(iSize==5) 
  { 
   if(!Check5Pai(m_MyPAIVec[4][0],m_MyPAIVec[4][1],m_MyPAIVec[4][2],m_MyPAIVec[4][3],m_MyPAIVec[4][4])) 
   { 
    return false; 
   } 
   else
   { 
    iJiangNum++ ; 
   } 
  } 
  else if(iSize==6) 
  { 
   if(!Check6Pai(m_MyPAIVec[4][0],m_MyPAIVec[4][1],m_MyPAIVec[4][2],m_MyPAIVec[4][3],m_MyPAIVec[4][4],m_MyPAIVec[4][5])) 
   { 
    return false; 
   } 
  } 
  else if(iSize==8) 
  { 
   if(!Check8Pai(m_MyPAIVec[4][0],m_MyPAIVec[4][1],m_MyPAIVec[4][2],m_MyPAIVec[4][3],m_MyPAIVec[4][4],m_MyPAIVec[4][5],m_MyPAIVec[4][6],m_MyPAIVec[4][7])) 
   { 
    return false; 
   } 
   else
   { 
    iJiangNum++ ; 
   } 
  } 
  else if(iSize==9) 
  { 
   if(!Check9Pai(m_MyPAIVec[4][0],m_MyPAIVec[4][1],m_MyPAIVec[4][2],m_MyPAIVec[4][3],m_MyPAIVec[4][4],m_MyPAIVec[4][5],m_MyPAIVec[4][6],m_MyPAIVec[4][7],m_MyPAIVec[4][8])) 
   { 
    return false; 
   } 
  } 
  else if(iSize==11) 
  { 
   if(!Check11Pai(m_MyPAIVec[4][0],m_MyPAIVec[4][1],m_MyPAIVec[4][2],m_MyPAIVec[4][3],m_MyPAIVec[4][4],m_MyPAIVec[4][5],m_MyPAIVec[4][6],m_MyPAIVec[4][7],m_MyPAIVec[4][8],m_MyPAIVec[4][9],m_MyPAIVec[4][10])) 
   { 
    return false; 
   } 
   else
   { 
    iJiangNum++ ; 
   } 
  } 
  else if(iSize==12) 
  { 
   if(!Check12Pai(m_MyPAIVec[4][0],m_MyPAIVec[4][1],m_MyPAIVec[4][2],m_MyPAIVec[4][3],m_MyPAIVec[4][4],m_MyPAIVec[4][5],m_MyPAIVec[4][6],m_MyPAIVec[4][7],m_MyPAIVec[4][8],m_MyPAIVec[4][9],m_MyPAIVec[4][10],m_MyPAIVec[4][11])) 
   { 
    return false; 
   } 
  } 
  else if(iSize==14) 
  { 
   if(!Check14Pai(m_MyPAIVec[4][0],m_MyPAIVec[4][1],m_MyPAIVec[4][2],m_MyPAIVec[4][3],m_MyPAIVec[4][4],m_MyPAIVec[4][5],m_MyPAIVec[4][6],m_MyPAIVec[4][7],m_MyPAIVec[4][8],m_MyPAIVec[4][9],m_MyPAIVec[4][10],m_MyPAIVec[4][11],m_MyPAIVec[4][12],m_MyPAIVec[4][13])) 
   { 
    return false; 
   } 
   else
   { 
    iJiangNum++ ; 
   } 
  } 
  else
  { 
   return false; 
  } 
 } 
  
 if(iJiangNum==1)return true; 
 return false; 
} 
//����� 
bool CMJ::CheckTING() 
{ 
 //���� 
 for(UINT j = 0 ; j < 9 ;j++ ) 
 { 
  //���� 
  AddPai(0,j+1); 
  if(CheckAllPai(MJPAI_GETPAI)) 
  { 
   int iPaiIndex = GetPaiIndex(0,j+1); 
   DelPai(iPaiIndex); 
   return true; 
  } 
  else
  { 
   int iPaiIndex = GetPaiIndex(0,j+1); 
   DelPai(iPaiIndex); 
  } 
 } 
 //���� 
 for(UINT j = 0 ; j < 9 ;j++ ) 
 { 
  //���� 
  AddPai(1,j+1); 
  if(CheckAllPai(MJPAI_GETPAI)) 
  { 
   int iPaiIndex = GetPaiIndex(1,j+1); 
   DelPai(iPaiIndex); 
   return true; 
  } 
  else
  { 
   int iPaiIndex = GetPaiIndex(1,j+1); 
   DelPai(iPaiIndex); 
  } 
 } 
 for(UINT i = 2 ; i < 5 ;i++ ) 
 { 
  for(UINT j = 0 ; j < 9 ;j++ ) 
  { 
   //���� 
   AddPai(i,j+1); 
   if(CheckAllPai(MJPAI_GETPAI)) 
   { 
    int iPaiIndex = GetPaiIndex(i,j+1); 
    DelPai(iPaiIndex); 
    return true; 
   } 
   else
   { 
    int iPaiIndex = GetPaiIndex(i,j+1); 
    DelPai(iPaiIndex); 
   } 
  } 
 } 
 return false; 
} 