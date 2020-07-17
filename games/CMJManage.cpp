#include "CMJManage.h" 
   
//���캯�� 
CMJManage::CMJManage() 
{ 
 m_HZPaiNum = 0; 
} 
//�������� 
CMJManage::~CMJManage() 
{ 
   
} 
  
//��ʼ���� 
void CMJManage::InitPai(int p_HZPaiNum) 
{ 
 m_HZPaiNum = p_HZPaiNum; 
 m_MJVec.clear(); 
 //�з��� 
 for(UINT i = 1 ; i <= 3 ; i++) 
 { 
  stPAI t_Pai; 
  t_Pai.m_Type = 0; 
  t_Pai.m_Value = i; 
  m_MJVec.push_back(t_Pai); 
  m_MJVec.push_back(t_Pai); 
  m_MJVec.push_back(t_Pai); 
  m_MJVec.push_back(t_Pai); 
 } 
 //�������� 
 for(UINT i = 1 ; i <= 4 ; i++) 
 { 
  stPAI t_Pai; 
  t_Pai.m_Type = 1; 
  t_Pai.m_Value = i; 
  m_MJVec.push_back(t_Pai); 
  m_MJVec.push_back(t_Pai); 
  m_MJVec.push_back(t_Pai); 
  m_MJVec.push_back(t_Pai); 
 } 
 //�� 
 for(UINT i = 1 ; i <= 9 ; i++) 
 { 
  stPAI t_Pai; 
  t_Pai.m_Type = 2; 
  t_Pai.m_Value = i; 
  m_MJVec.push_back(t_Pai); 
  m_MJVec.push_back(t_Pai); 
  m_MJVec.push_back(t_Pai); 
  m_MJVec.push_back(t_Pai); 
 } 
 //�� 
 for(UINT i = 1 ; i <= 9 ; i++) 
 { 
  stPAI t_Pai; 
  t_Pai.m_Type = 3; 
  t_Pai.m_Value = i; 
  m_MJVec.push_back(t_Pai); 
  m_MJVec.push_back(t_Pai); 
  m_MJVec.push_back(t_Pai); 
  m_MJVec.push_back(t_Pai); 
 } 
 //�� 
 for(UINT i = 1 ; i <= 9 ; i++) 
 { 
  stPAI t_Pai; 
  t_Pai.m_Type = 4; 
  t_Pai.m_Value = i; 
  m_MJVec.push_back(t_Pai); 
  m_MJVec.push_back(t_Pai); 
  m_MJVec.push_back(t_Pai); 
  m_MJVec.push_back(t_Pai); 
 } 
 XiPai(); 
} 
  
//ϴ�� 
void CMJManage::XiPai() 
{ 
 srand( GetTickCount() ); 
 random_shuffle(m_MJVec.begin(),m_MJVec.end()); 
} 
   
//���� 
stPAIEx CMJManage::GetAPai() 
{ 
 //��������ƶ������� 
   
 stPAIEx t_Pai; 
 t_Pai.m_NewPai.m_Type = m_MJVec.back().m_Type; 
 t_Pai.m_NewPai.m_Value = m_MJVec.back().m_Value; 
 t_Pai.m_PaiNum = m_MJVec.size()-1; 
 if(t_Pai.m_PaiNum ==m_HZPaiNum) 
 { 
  t_Pai.m_IsHZ = true; 
 } 
 else
 { 
  t_Pai.m_IsHZ = false; 
 } 
 //��ȥһ�� 
 m_MJVec.pop_back(); 
 return t_Pai; 
} 