#ifndef _CMJMANAGE_H 
#define _CMJMANAGE_H 
#include "CMJ.h" 
//ʣ����ǽ��Ϣ 
//��չ 
struct stPAIEx 
{ 
 stPAI m_NewPai;      //������� 
 int  m_PaiNum;      //ʣ������ 
 bool m_IsHZ;       //�Ƿ��ׯ 
} 
; 
  
//�齫������ 
class CMJManage 
{ 
 vector<stPAI> m_MJVec;    //�齫����VEC 
 int    m_HZPaiNum;    //��ׯ������ 
public: 
  
 //���캯�� 
 CMJManage(); 
 //�������� 
 ~CMJManage(); 
 //��ʼ���� 
 void InitPai(int p_HZPaiNum = 0); 
 //���� 
 stPAIEx GetAPai(); 
private: 
 //ϴ�� 
 void XiPai(); 
} 
; 
  
#endif 