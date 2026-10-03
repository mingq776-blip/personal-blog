import { Canvas, useFrame } from "@react-three/fiber";
import { useEffect, useMemo, useRef, useState } from "react";
import * as THREE from "three";

type SceneProps = {
  mobile: boolean;
  reduced: boolean;
};

function ParticleScene({ mobile, reduced }: SceneProps) {
  const group = useRef<THREE.Group>(null);
  const core = useRef<THREE.Group>(null);
  const count = reduced ? 380 : mobile ? 720 : 1550;

  const { positions, linePositions } = useMemo(() => {
    let seed = 20261003;
    const random = () => {
      seed = (seed * 1664525 + 1013904223) % 4294967296;
      return seed / 4294967296;
    };

    const positions = new Float32Array(count * 3);
    const radialPoints: THREE.Vector3[] = [];

    for (let index = 0; index < count; index += 1) {
      const theta = random() * Math.PI * 2;
      const phi = Math.acos(2 * random() - 1);
      const wobble = Math.sin(theta * 3 + phi * 4) * 0.13 + (random() - 0.5) * 0.16;
      const radius = 2.05 + wobble;
      const x = radius * Math.sin(phi) * Math.cos(theta);
      const y = radius * Math.cos(phi) * 1.08;
      const z = radius * Math.sin(phi) * Math.sin(theta);
      positions[index * 3] = x;
      positions[index * 3 + 1] = y;
      positions[index * 3 + 2] = z;
      if (index < 110) radialPoints.push(new THREE.Vector3(x, y, z));
    }

    const lines: number[] = [];
    radialPoints.forEach((point, index) => {
      for (let targetIndex = index + 1; targetIndex < radialPoints.length; targetIndex += 1) {
        const target = radialPoints[targetIndex];
        if (point.distanceTo(target) < 0.48) {
          lines.push(point.x, point.y, point.z, target.x, target.y, target.z);
        }
      }
    });

    return { positions, linePositions: new Float32Array(lines) };
  }, [count]);

  useFrame((state, delta) => {
    if (!group.current) return;
    const speed = reduced ? 0.0015 : 0.004;
    group.current.rotation.y += delta * speed * (mobile ? 0.65 : 1);
    group.current.rotation.x = THREE.MathUtils.lerp(group.current.rotation.x, state.pointer.y * 0.12, 0.035);
    group.current.rotation.z = THREE.MathUtils.lerp(group.current.rotation.z, -state.pointer.x * 0.08, 0.035);
    if (core.current && !reduced) {
      core.current.rotation.x += delta * 0.08;
      core.current.rotation.y += delta * 0.11;
      core.current.position.y = Math.sin(state.clock.elapsedTime * 0.9) * 0.08;
    }
  });

  return (
    <group ref={group}>
      <points>
        <bufferGeometry>
          <bufferAttribute attach="attributes-position" args={[positions, 3]} />
        </bufferGeometry>
        <pointsMaterial color="#62e6cf" size={mobile ? 0.017 : 0.013} sizeAttenuation transparent opacity={0.72} depthWrite={false} blending={THREE.AdditiveBlending} />
      </points>
      <lineSegments>
        <bufferGeometry>
          <bufferAttribute attach="attributes-position" args={[linePositions, 3]} />
        </bufferGeometry>
        <lineBasicMaterial color="#8ff8e5" transparent opacity={0.13} blending={THREE.AdditiveBlending} />
      </lineSegments>
      <group ref={core}>
        <mesh rotation={[0.4, 0.7, 0.15]}>
          <icosahedronGeometry args={[1.08, 2]} />
          <meshBasicMaterial color="#f4c46b" wireframe transparent opacity={0.11} />
        </mesh>
      </group>
      <mesh scale={1.75}>
        <sphereGeometry args={[1, 32, 32]} />
        <meshBasicMaterial color="#071827" transparent opacity={0.08} side={THREE.BackSide} />
      </mesh>
    </group>
  );
}

export default function ParticleCanvas({ reduced }: { reduced: boolean }) {
  const [mobile, setMobile] = useState(false);

  useEffect(() => {
    setMobile(window.matchMedia("(max-width: 768px)").matches);
  }, []);

  return (
    <Canvas camera={{ position: [0, 0, 7.2], fov: 42 }} dpr={[1, mobile ? 1.15 : 1.5]} gl={{ antialias: false, alpha: true, powerPreference: "high-performance" }}>
      <ParticleScene mobile={mobile} reduced={reduced} />
    </Canvas>
  );
}
