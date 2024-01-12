package com.spring.member.service;

import com.spring.member.dto.MemberDTO;
import com.spring.member.entity.MemberEntity;
import com.spring.member.repository.MemberRepository;
import java.util.Optional;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class MemberService {
    private final MemberRepository memberRepository;

    public void save(MemberDTO memberDTO) {
        // repository 의 save 메서드 호출 (entity 객체를 넘겨줘야함)
        // 1. dto -> entity 변환
        // 2. repository 의 save 메서드 호출
        MemberEntity memberEntitiy = MemberEntity.toMemberEntitiy(memberDTO);
        memberRepository.save(memberEntitiy);

    }

    public MemberDTO login(MemberDTO memberDTO) {
        // 1. 회원이 입력한 이메일로 DB에서 조회
        // 2. DB에서 조회한 비밀번호와 사용자가 입력한 비밀번호가 일치하는지 판단
        Optional<MemberEntity> byMemberEmail = memberRepository.findByMemberEmail(memberDTO.getMemberEmail());
        if (byMemberEmail.isPresent()) {
            // 조회 결과가 있다면?( 회원가입된 이메일 이라면 )
            MemberEntity memberEntity =byMemberEmail.get();
            if (memberEntity.getMemberPassword().equals(memberDTO.getMemberPassword())) {
                //비밀번호 일치할 시
                // entity 객체를 dto로 변환 후 리턴
                MemberDTO dto = MemberDTO.toMemberDTO(memberEntity);
                return dto;
            } else {
                // 비밀번호 불일치
                return null;
            }
        } else {
            // 조회 결과가 없다면( 회원가입 되지 않은 이메일이라면 )

            return null;
        }
    }
}
